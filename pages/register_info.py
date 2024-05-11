from flet import *

class Register_Info(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.alignment= alignment.center        
        self.expand = True
        self.bgcolor = "#3778c2"
    
        self.user_weight = Container(
            content= TextField(
                border=InputBorder.NONE,
                label="Weight (kg)",
                text_align="left",
                bgcolor='#fffafa',
                input_filter= NumbersOnlyInputFilter(),
                hint_text="Please input a number"
            )
        )
        
        self.user_height = Container(
            content= TextField(
                border=InputBorder.NONE,
                label="Height (cm)",
                text_align="left",
                bgcolor='#fffafa',
                input_filter= NumbersOnlyInputFilter(),
                hint_text="Please input a number"
            )            
        )
          
        self.user_weight_goal  = Container(
            content= TextField(
                border=InputBorder.NONE,
                label="Weight Goal (kg)",
                text_align="left",
                bgcolor='#fffafa',
                input_filter= NumbersOnlyInputFilter(),
                hint_text="Please input a number"
            )
        )  
        self.content = Column(
            alignment='center',
            horizontal_alignment='center',
            controls=[
                Container(
                    width=500,
                    height=1000,
                    padding=50,
                    bgcolor="#ffffff",
                    content=Column(
                        horizontal_alignment='center',
                        controls=[
                            Text(
                                "Personal Information", size="24"
                            ),
                            self.user_weight, self.user_height, self.user_weight_goal,
                            Container(
                                alignment=alignment.center,
                                height=40,
                                bgcolor='#c0c0c0',
                                border_radius=30, 
                                content=Text(
                                    value='Save',
                                ),
                                on_click=lambda e: self.page.go(
                                    '/dashboard'
                                )
                            )
                        ]
                    )
                )
            ]
        )
       
