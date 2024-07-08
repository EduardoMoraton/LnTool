import flet as ft
from core.LnTool import LnTool
from app_layout import AppLayout

class LnToolApp(ft.UserControl):
    def __init__(self, page: ft.Page, core: LnTool):
        super().__init__()
        self.core = core
        self.page = page
        self.appbar_items = [
            ft.PopupMenuItem(text="Clear sessions"),
        ]
        self.appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=ft.Text("LnTool",size=32, text_align="start"),
            center_title=False,
            toolbar_height=75,
            bgcolor=ft.colors.PURPLE_300,
            actions=[
                ft.Container(
                    content=ft.PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=ft.margin.only(left=50, right=25)
                )
            ],
        )
        self.page.appbar = self.appbar
        self.expand = True
    
    
    def build(self):
        self.layout = AppLayout(self, self.page)
        return self.layout