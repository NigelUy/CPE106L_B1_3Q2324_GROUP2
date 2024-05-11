from flet import *
from pages.login import Login
from pages.register import Register
from pages.dashboard import Dashboard
from pages.register_info import Register_Info
class Main(Control):
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
            "/dashboard": Dashboard,
            "/register_info": Register_Info,
            #"/person_info": person_info,
        }[self.page.route](self.page)

        self.page.views.clear()
        self.page.views.append(
            View(
                route,
                [new_page]
            )
        )
        self.page.update()

app(target = Main, assets_dir='assets')