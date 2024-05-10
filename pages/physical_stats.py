from flet import *

class Physical_Stats(Container):
    def  __init__(self, page: Page): #static dashboard
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
                                    src="Login\\Logo1.png",
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
                ), #static dashboard
            ]
        )
            
