from flet import *

class Register(Container):
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
            )
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
        self.re_password = Container(
            content = TextField(
                border= InputBorder.NONE,
                label='Re-enter Password',
                text_align='left',
                bgcolor='#fffafa',
                password=True
            )
        )        

        self.submit_button = Container(
            content = ElevatedButton(
                text='Login',

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
                                value='Register',
                                size=50,
                                text_align='center',
                                weight = 'bold',
                            ),
                            self.username,
                            self.password,
                            self.re_password,
                            Container(
                                content = Text(
                                    value='Already have an account? Login',
                                    color='#4b9fe1',
                                ),
                                on_click=lambda e: self.page.go(
                                    '/login'
                                )
                            ),
                            self.submit_button
                        ]
                    )
                )
            ]
        )