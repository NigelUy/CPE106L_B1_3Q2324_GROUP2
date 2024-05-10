from flet import *
from mealgeneration.meal_generation import person_info


class Dashboard(Container):
    def  __init__(self, page: Page):
        super().__init__()
        self.expand = True
        self.bgcolor = '#63bce5'

        self.content = Row(
            controls= [
                Container(
                    width=200,
                    bgcolor='#dcdcdc',
                    padding=padding.only(top=20, left=10, right=10),
                    content= Column(
                        controls=[
                            Container(
                                Image(
                                    src="resources\\Logo1.png",
                                    width=100,
                                    height=100,
                                    fit=ImageFit.COVER
                                    )
                            ),
                            Container(
                                Divider()
                            ),
                            ListTile(
                                leading=Icon(icons.DASHBOARD, size=24),
                                title=Text(
                                    value="Dashboard",
                                    size=20,
                                ),
                                on_click=lambda e: self.page.go(
                                    "/dashboard"
                                )
                            ),
                            ListTile(
                                leading=Icon(icons.SHOPPING_BASKET, size=24),
                                title=Text(
                                    value="Groceries",
                                    size=20,
                                )
                            ),
                            ListTile(
                                leading=Icon(icons.STACKED_BAR_CHART, size=24),
                                title=Text(
                                    value="Physical Stats",
                                    size=20,
                                ),
                                on_click=lambda e: self.page.go(
                                    "/physical_stats"
                                )                                
                            ),                            
                        ]
                    )
                ),
                Container( #2nd member of the row
                    expand=True,
                    content=Column( #header
                        expand=True,
                        controls=[
                            Container(
                                height=50,
                                bgcolor='#ffffff',
                                padding=padding.only(top=10,bottom=20)
                            ),
                            Column( #lower part
                                expand=True,
                                scroll=True,
                                horizontal_alignment='center',    
                                controls=[
                                    Container(
                                        alignment=alignment.center,
                                        height=100,
                                        bgcolor='#b0c4de',
                                        border_radius=50,
                                        content=Text(
                                            value='Generate a Meal Plan',
                                            size=24
                                        ),
                                        on_click=lambda e: self.page.go(
                                            "/person_info"
                                        )
                                    )
                                ]
                            )
                        ]
                    )
                )
            ]
        )
