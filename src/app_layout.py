import flet as ft
from nav_rail import NavRail


class AppLayout(ft.UserControl):
    def __init__(self,
                 app, 
                 page: ft.Page, 
    ):
        super().__init__()
        self.page = page
        self.app = app
        

    def build(self):
        self.rail = NavRail(self.app, self.page)
        self.row = ft.Row(
            controls=[
                self.rail,
                ft.VerticalDivider(width=1),
                ft.Column([ ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
        )
        return self.row
