import flet as ft
submission_row = None


def main(page: ft.Page):
    page.navigation_bar = ft.NavigationBar(
        bgcolor="blue",
        selected_index=0,
        destinations=[ft.NavigationDestination(icon="home")]
    )

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

    def meal_Type(meal_num):
        meal = []
        meal_num = int(meal_num)
        meal_index = 0


        def move(index):
            nonlocal meal_index
            meal_index = index
            for col in meal:
                col.visible = (meal.index(col) == meal_index)
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
            for col in meal: #clear visibility
                col.visible = False
            page.add(submission_row)
            page.update()

            ##additional code for keeping the variables

        for i in range(meal_num):
            meal.append(ft.Column(
                controls=[
                    ft.Text(value="MEAL " + str(i + 1) + ": "),
                    ft.Checkbox(label="Breakfast", value=False),
                    ft.Checkbox(label="Lunch", value=False),
                    ft.Checkbox(label="Dinner", value=False),
                    ft.Checkbox(label="Snacks", value=False),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="Previous",
                                icon="arrow_back",
                                disabled=i == 0,
                                on_click=lambda e, index=i: move(index - 1)
                            ),
                            ft.ElevatedButton(
                                text="Next" if i < meal_num - 1 else "Submit",
                                icon="arrow_forward",
                                on_click=lambda e, index=i: submit() if index == meal_num - 1 else move(index + 1)
                            )
                        ],
                    )
                ],
                visible=False  # Initially set all to not visible
            ))

        move(0)  # Set initial visibility
        return meal  # Return the list of meal controls, not the result of move()

    page.add(
        information(1000, 3),
        *meal_Type(3)  # Use the asterisk (*) to unpack the list of controls
    )


ft.app(target=main)