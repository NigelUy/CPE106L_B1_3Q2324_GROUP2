from flet import *
from login import Login
from register import Register

class Main(UserControl):
    def __init__(self, page: Page,):
        self.page = page
        self.init_helper()

    def init_helper(self,):
        self.page.on_route_change = self.on_route_change
        self.page.go('/login')
        
    def on_route_change(self, route):
        new_page = {
            "/login": Login,
            "/register": Register,
        }[self.page.route](self.page)

        self.page.views.clear()
        self.page.views.append(
            View(
                route,
                [new_page]
            )
        )
        self.page.update()

app(target = Main)