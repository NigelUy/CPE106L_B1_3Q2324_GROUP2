import flet as ft
import pandas as pd
submission_row = None


def information(calorie_goal, number_of_meals):
    return ft.Row(
        controls=[
            ft.Container(
                content=ft.Text(value="CALORIE GOAL: ", size=50, weight=ft.FontWeight.BOLD, italic=True),
            ),
            ft.Container(
                content=ft.Text(value=str(calorie_goal), size=50, italic=True),
                border=ft.border.all(2),
                padding=10
            ),
            ft.Container(
                content=ft.Image(src="Blender.png", fit=ft.ImageFit.SCALE_DOWN, width=100, height=100),
                expand=True
            ),
            ft.Container(
                content=ft.Text(value="MEAL COUNT: ", size=50, italic=True, weight=ft.FontWeight.BOLD),
                alignment=ft.alignment.center
            ),
            ft.Container(
                content=ft.Text(value=str(number_of_meals), size=50, italic=True),
                alignment=ft.alignment.center,
                padding=10,
                border=ft.border.all(2),
            ),
        ],
    )

def create_datatables():
    table=ft.DataTable(
        expand=True,
        border=ft.border.all(2, "black"),
        show_bottom_border=True,

        columns=[
                ft.DataColumn(ft.Text("Meal Type")),
                ft.DataColumn(ft.Text("Meal_name")),
                ft.DataColumn(ft.Text("Calories")),
                ft.DataColumn(ft.Text("Ingredients")),
                ft.DataColumn(ft.Text("Description")),
            ],
        rows=[
            ft.DataRow([
                ft.DataCell(ft.Text(f"Snack")),
                ft.DataCell(ft.Text("UNGABUNGA")),
                ft.DataCell(ft.Text(f"1000")),
                ft.DataCell(ft.Text(f"Apples,bananasApplesApplesApplesApplesApplesApplesApplesApplesApplesApplesApplesApplesApplesApplesApplesApples")),
                ft.DataCell(ft.Text(f"horrid")),
            ]) for i in range(100)  # Test with 100 rows
        ]
        )
    cv = ft.Column([table])
    rv = ft.Row([cv],scroll=True,  vertical_alignment=ft.CrossAxisAlignment.START)
    return rv
def ui(page: ft.Page):

    page.navigation_bar = ft.NavigationBar(
        bgcolor="blue",
        selected_index=0,
        destinations=[ft.NavigationDestination(icon="home")]
    )


    def meal_Type(meal_num):
        meal = []
        checkbox_states_list = []
        meal_num = int(meal_num)
        meal_index = 0
        checkbox_states = [{"MEAL_ID": f"meal_{i}", "breakfast": None, "lunch": None, "dinner": None, "snacks": None} for i in range(meal_num)]

        alerts = ft.AlertDialog(
            title=ft.Text("Checkbox missing"), content=ft.Text("Please select one"), on_dismiss=lambda e: print("Dialog dismissed!")
        )


        def check_current_page(index):
            """ Check if at least one checkbox on the current page is checked """
            # Extract the relevant checkbox states for the current meal
            nonlocal checkbox_states_list
            current_meal_checkboxes = checkbox_states[index]
            first = True
            for value in current_meal_checkboxes.values():
                if first:
                    first = False
                    continue
                if value:
                    return True
            return False

        def move(index):
            nonlocal meal_index
            if check_current_page(meal_index):
                meal_index = index
                for row in meal:
                    row.visible = (meal.index(row) == meal_index)
                page.update()


        def handle_button_click(e, index):
            if check_current_page(index):
                if index == meal_num - 1:
                    submit()
                else:
                    move(index + 1)
            else:
                page.dialog = alerts
                alerts.open = True
                page.update()

        def submit():
            global submission_row

            def back_to_edit(e):
                submission_row.visible = False
                move(0)  # Move back to the first meal entry when "Edit" is clicked
                page.update()

            if submission_row is None:
                submission_row = ft.Row(
                    controls=[
                        ft.Text(value="Meals submitted", size=50, italic=True, weight=ft.FontWeight.BOLD),
                        ft.ElevatedButton(
                            text="Edit",
                            icon="edit_sharp",
                            on_click=back_to_edit,  # Attach the correct event handler function
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    visible=True
                )
                page.add(submission_row)
            else:
                submission_row.visible = True
            for col in meal:  #clear visibility
                col.visible = False
            page.add(submission_row)
            page.update()

            ##additional code for keeping the variables

        for i in range(meal_num):
            # Wrap each checkbox with a Container to control alignment
            checkboxes = [
                ft.Container(
                    content=ft.Checkbox(
                        label="Breakfast", value=False,
                        on_change=lambda e, index=i, id="breakfast": checkbox_states[index].update(
                            {id: e.control.value})
                    ),
                    alignment=ft.alignment.center  # Center align the checkbox within the container
                ),
                ft.Container(
                    content=ft.Checkbox(
                        label="Lunch", value=False,
                        on_change=lambda e, index=i, id="lunch": checkbox_states[index].update({id: e.control.value})
                    ),
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=ft.Checkbox(
                        label="Dinner", value=False,
                        on_change=lambda e, index=i, id="dinner": checkbox_states[index].update({id: e.control.value})
                    ),
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=ft.Checkbox(
                        label="Snacks", value=False,
                        on_change=lambda e, index=i, id="snacks": checkbox_states[index].update({id: e.control.value})
                    ),
                    alignment=ft.alignment.center
                )
            ]
            meal.append(ft.Row(
                controls=[ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(value="MEAL " + str(i + 1) + ": ", weight=ft.FontWeight.BOLD,),
                            *checkboxes,
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton(
                                        text="Previous",
                                        icon="arrow_back",
                                        disabled=i == 0,
                                        on_click=lambda e, index=i - 1: move(index)
                                    ),
                                    ft.ElevatedButton(
                                        text="Next" if i < meal_num - 1 else "Submit",
                                        icon="arrow_forward",
                                        on_click=lambda e, index=i: handle_button_click(e, index)
                                    )
                                ],
                                alignment=ft.alignment.center
                            )
                        ],
                    ),
                    alignment=ft.alignment.center,  # Control the alignment as required
                )
                ],
                visible=True if i == 0 else False,
                alignment=ft.MainAxisAlignment.CENTER

            ))
            # Then append the column to the meals list
        move(0)  # Set initial visibility
        return meal  # Return the list of meal controls, not the result of move()

    page.add(
        ft.Column(expand=True,scroll=ft.ScrollMode.ALWAYS, controls=[
            information(1000, 3),
            *meal_Type(3),  # Use the asterisk (*) to unpack the list of controls
            create_datatables()
        ])
    )


ft.app(target=ui)

