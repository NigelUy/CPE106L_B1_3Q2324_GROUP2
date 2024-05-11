from flet import *
from resources.validator import Validator
from database import db_path
from database.crud import *
from database.database import create_database
import time

class Login(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.alignment = alignment.center
        self.expand = True
        self.bgcolor = "#3778c2"
        self.validator = Validator()
        
        self.error_border = border.all(width=3, color = "#ff0000")
        self.error_field = Text(value="", color="#ff0000", size = 16)

        self.email = Container(
            content = TextField(
                border= InputBorder.NONE,
                label='Email',
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

        self.submit_button = Container(
            content = ElevatedButton(
                text='Login',
                on_click=self.login,
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
                                color = "#000000"
                            ),
                            self.error_field,
                            self.email,
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
                            self.submit_button
                        ]
                    )
                )
            ]
        )

    def login(self, e):
        email_value = self.email.content.value
        password_value = self.password.content.value

        if email_value and password_value:
            conn = connect_to_database(db_path)

            if not self.validator.is_valid_email(email_value):
                self.email.border =self.error_border
                self.error_field.value = "Enter a valid email"
                self.error_field.size = 12
                self.error_field.update()
                self.email.update()
                time.sleep(1.5)
                self.email.border = InputBorder.NONE
                self.error_field.value =""
                self.error_field.update()
                self.email.update()
                
            elif check_data_exists(conn, "user", f"email='{email_value}'"):
                get_user = get_data(conn, "user", f"email='{email_value}'")
                is_email_match = get_user[0]["email"] == email_value
                is_password_match = get_user[0]["password"] == password_value

                if is_email_match and is_password_match:
                    self.page.splash = ProgressBar()
                    self.page.update()
                    time.sleep(2)
                    self.page.splash = None
                    self.page.go("/dashboard")

                else:
                    self.password.border = self.error_border
                    self.email.border = self.error_border
                    self.error_field.value = "Email or Password is Incorrect"
                    self.password.update()
                    self.email.update()
                    self.error_field.update()
                    time.sleep(2)
                    self.password.border = InputBorder.NONE
                    self.email.border = InputBorder.NONE
                    self.error_field.value = ""
                    self.password.update()
                    self.email.update()
                    self.error_field.update()
        else:
            self.error_field.value = "All fields should be filled up"
            self.error_field.size = 16
            self.error_field.update()
            time.sleep(2)
            self.password.border = InputBorder.NONE
            self.email.border = InputBorder.NONE
            self.error_field.value = ""
            self.password.update()
            self.email.update()            
            self.error_field.update()            