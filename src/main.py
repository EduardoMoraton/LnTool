import flet as ft

from core.LnTool import LnTool
from lnTool_app import LnToolApp
 
if __name__ == "__main__":
 
    def main(page: ft.Page):
        

        page.title = "LnTool"
        
        core = LnTool("./driver/chromedriver", "./cookie/")
        core.set_session(0)
        core.load_session()
        core.load_works("junior", "Alicante")
        
        app = LnToolApp(page, core)
        page.add(app)
        page.update()
        
        def client_exit():
            core.close()
        page.on_close = client_exit
 
    ft.app(target=main)