import flet as ft
from core.LnTool import LnTool

class SessionItem(ft.UserControl):
    def __init__(self,
                 user,
                 index,
                 manager):
        super().__init__()
        self.user = user
        self.index = index
        self.manager = manager
        self.card = ft.Card(
                    content=ft.Container(
                        content=ft.Row(
                            [
                                ft.ListTile(
                                    leading=ft.Icon(ft.icons.PEOPLE),
                                    title=ft.Text(user),
                                    width=300
                                ),
                                ft.Row(
                                    [ 
                                        ft.IconButton(icon=ft.icons.DELETE, on_click=self.handle_cookie_delete),
                                        ft.IconButton(icon=ft.icons.ARROW_CIRCLE_RIGHT, on_click=self.handle_cookie_selection)
                                    ]
                                )
                               
                            ],
                        ),
                        width=400,
                        padding=5
                    ),
        
        )
    

    def build(self):
        return self.card
    
    def handle_cookie_delete(self, e):
        self.manager.handle_cookie_delete(self.index)
    def handle_cookie_selection(self, e):
        self.manager.handle_cookie_selection(self.index)

class NavRail(ft.UserControl):
    def __init__(self, 
                 app, 
                 page: ft.Page, ):
        super().__init__()
        self.app = app
        self.page = page

        self.dlg = ft.AlertDialog(
            title=ft.Text("Session manager"),
            modal=True
        )
        self.avatar = ft.CircleAvatar()

    def build(self):
        self.rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        expand=True,
        min_width=100,
        min_extended_width=400,
        leading=ft.Row(controls=[
            self.avatar,
            ft.IconButton(icon=ft.icons.CREATE,
                          on_click=self.change_session)
            ]),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="First"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Second",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Settings"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )
        return self.rail
    
    def avatar_control(self, avatar):
        self.avatar.background_image_url = avatar
        self.avatar.update()
    
    def handle_cookie_selection(self, index):
        self.dlg.open = False
        self.app.core.set_session(index)
        self.app.core.load_session()
        self.avatar_control(self.app.core.current_session_avatar())
        self.update()
        self.dlg.open = False
        self.page.update()
        
        
    def handle_cookie_delete(self, index):
        self.dlg.open = False
        self.page.update()
        
    def change_session(self, x):
        
        obj = []
        
        for (i, it) in enumerate(self.app.core.sesions):
            obj.append(SessionItem(it, i, self))
        
        dialog_content = ft.Column(
            width=400,
            controls=obj
        )
        
        self.dlg.content = dialog_content
        
        self.page.dialog = self.dlg
        self.dlg.open = True
        self.page.update()
        