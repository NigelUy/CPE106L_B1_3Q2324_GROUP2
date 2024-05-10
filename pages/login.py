from flet import *

class Login(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.alignment = alignment.center
        self.expand = True
        self.bgcolor = "#3778c2"

        self.username = Container(
            content = TextField(
                border= InputBorder.NONE,
                label='Username',
                text_align='left',
                bgcolor='#fffafa'
            ),
            border=border.all(width=1, color='#bdcbf4'),
        )

        self.password = Container(
            content = TextField(
                border= InputBorder.NONE,
                label='Password',
                text_align='left',
                bgcolor='#fffafa',
                password=True
            )
        )

        self.submit_button = Container(
            on_click= lambda e: self.page.go('dashboard'),
            alignment='center',
            height=5,
            border_radius=5,
            content = Text(
                "Submit",
            )
        )        

        self.content = Column(
            alignment='center',
            horizontal_alignment='center',
            controls=[
                Container(
                    width= 800,
                    padding=50,
                    bgcolor="#ffffff",
                    content= Column(
                        horizontal_alignment='center',
                        controls=[
                            Text(
                                value='Meal Planner v0.1',
                                size=50,
                                text_align='center',
                                weight = 'bold',
                            ),
                            self.username,
                            self.password,
                            Container(
                                content = Text(
                                    value='Not Yet Registered?',
                                    color='#4b9fe1',
                                ),
                                on_click=lambda e: self.page.go(
                                    '/register'
                                )
                            ),
                            Container(
                                alignment=alignment.center,
                                height=40,
                                bgcolor='#c0c0c0',
                                border_radius=30, 
                                content=Text(
                                    value='Login',
                                ),
                                on_click=lambda e: self.page.go(
                                    '/dashboard',
                                ),
                            ),
                        ]
                    )
                )
            ]
        )

       # def login(self, e):
            #if not self.validator.is_valid_