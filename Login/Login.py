import flet as ft
from flet import TextField, ElevatedButton, Text, Row, Column, UserControl
from flet_core.control_event import ControlEvent

class Login(UserControl):
    def __init__(self, page: ft.Page):
        self.page = page 

        self.text_username = TextField(label = 'Username', text_align=ft.TextAlign.LEFT)
        self.text_password = TextField(label = 'Password', text_align=ft.TextAlign.LEFT, password=True)
        self.unregistered = 
        self.button_submit = ElevatedButton(text='Login', disabled=True)

        self.event_handlers()

    def event_handlers(self):
        self.text_username.on_change = self.validate
        self.text_password.on_change = self.validate
        self.button_submit.on_click = self.submit

    def validate(self, e: ControlEvent) -> None:
        if all([self.text_username.value, self.text_password.value]):
            self.button_submit.disabled = False
        else:
            self.button_submit.disabled = True
        self.page.update()

    def submit(self, e: ControlEvent) -> None:
        print('Username: ', self.text_username.value)
        print('Password: ', self.text_password.value)

        self.page.clean()
        self.page.add(
            Row(
                controls = [Text(value=f'Welcome, {self.text_username.value}', size=30)],
                alignment = ft.MainAxisAlignment.CENTER
            )
        )

    
    def UI_form(self) -> Row:
        return Row(
            controls= [
                Column(
                    [self.text_username,
                    self.text_password, 
                    self.button_submit]
                )
            ],
             alignment=ft.MainAxisAlignment.CENTER
        ) 

    

def main(page: ft.Page) -> None:
    page.title = 'Login'
    page.padding = 0
    page.window_resizable = False
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    login = Login(page)

    page.add(login.UI_form())

ft.app(target=main)