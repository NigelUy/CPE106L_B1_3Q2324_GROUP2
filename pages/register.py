from flet import *
from resources.validator import Validator
from database.crud import *
from database import db_path
from database.hash_password import *
import time

class Register(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.alignment = alignment.center
        self.expand = True
        self.validator = Validator()
        self.bgcolor = "#3778c2"
        
        self.error_border = border.all(width=12, color = "#ff0000")
        self.error_field = Text(value="adfadfasdfs", color="#ff0000", size = 16)

        self.first_name = Container(
            content = TextField(
                border= border.all(),
                label='First name',
                text_align='left',
                bgcolor='#fffafa'
            )
        )

        self.last_name = Container(
            content = TextField(
                border= border.all(),
                label='Last name',
                text_align='left',
                bgcolor='#fffafa'
            )
        )

        self.email = Container(
            content = TextField(
                border= border.all(),
                label='Email',
                text_align='left',
                bgcolor='#fffafa'
            )
        )

        self.password = Container(
            content = TextField(
                border= border.all(),
                label='Password',
                text_align='left',
                bgcolor='#fffafa',
                password=True
            )
        )
        self.re_password = Container(
            content = TextField(
                border= border.all(),
                label='Re-enter Password',
                text_align='left',
                bgcolor='#fffafa',
                password=True
            )
        )        

        self.submit_button = Container(
            content = ElevatedButton(
                text='Register',
                on_click=self.register,
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
                            self.error_field,
                            self.first_name,
                            self.last_name,
                            self.email,
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

    def register(self, e):
        self.error_field.value = "pls gumana ka"
        print("pls")
        first_name_value = self.first_name.content.value
        last_name_value = self.last_name.content.value
        email_value = self.email.content.value
        password_value = self.password.content.value
        re_password_value = self.re_password.content.value

        if first_name_value and last_name_value and email_value and password_value and re_password_value:
            conn = connect_to_database(db_path)

            if not self.validator.is_valid_email(email_value):
                self.email.border =self.error_border
                self.error_field.value = "Enter a valid email"
                self.error_field.size = 12
                self.error_field.update()
                self.email.update()
                time.sleep(1.5)
                self.email.border = self.default_border
                self.error_field.size = 1
                self.error_field.update()
                self.email.update()

            elif not check_data_exists(conn, "user", f"email='{email_value}'"):
                insert_data(
                    conn,
                    "user",
                    (first_name_value, last_name_value, email_value, password_value)
                )
                self.page.spash =ProgressBar()
                self.error_field.value = "You have successfully registered"
                self.error_field.color = 'green'
                self.error_field.size = 12
                self.page.update()
                time.sleep(1.5)
                self.page.splash = None
                self.page.upate()
                self.page.go("/login")
            else:
                self.email.border =self.error_border
                self.error_field.value = "Email already exists"
                self.error_field.size = 12
                self.error_field.update()
                self.email.update()
                time.sleep(1.5)
                self.email.border = self.default_border
                self.error_field.size = 1
                self.error_field.update()
                self.email.update()

        else:
            self.error_field.value = "All fields should be filled up"
            self.error_field.size = 16
            self.error_field.update()
            time.sleep(1.5)
            self.error_field.size = 0
            self.error_field.update()
