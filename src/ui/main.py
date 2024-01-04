from ui.Sidebar import Sidebar
from ui.Titlebar import Titlebar
from ui.Footer import Footer
from ui.WelcomeScreen import WelcomeScreen
import customtkinter as ctk


class UI(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("CTk Example")
        self.geometry("800x620")
        self.resizable(False, False)
        self.sidebar = Sidebar(self)
        self.titlebar = Titlebar(self)
        self.footer = Footer(self)
        self.welcome_screen = WelcomeScreen(self)

        self.sidebar.set_button_pressed(0)

    def run(self):
        self.mainloop()
