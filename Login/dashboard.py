from flet import *

class Dashboard(Container):
    def  __init__(self, page: Page):
        super().__init__()
        self.expand = True
        self.bgcolor = '#63bce5'

        self.content = Row(
            controls= [
                Container(
                    width=120,
                    bgcolor='#ffffff',
                    padding=padding.only(top=20, left= 10, right=10),
                    content= Column(
                        controls=[
                            Row(
                                controls=[
                                    Icon(
                                        icons.PERSON,
                                        size= 30
                                    )
                                ]
                            ),
                            Container(
                                Text(
                                value="Dashboard",
                                size=20,
                                color="#63bce5"
                                )
                            )
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
                                controls=[

                                    Container(
                                        content=FilledButton(
                                            icon='add',
                                            text="Generate Meal Plan"
                                        )
                                    )
                                ]
                            )
                        ]
                    )
                )
            ]
        )
