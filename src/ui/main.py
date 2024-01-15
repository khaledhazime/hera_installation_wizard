import customtkinter as ctk
from ui.Sidebar import Sidebar
from ui.Titlebar import Titlebar
from ui.Footer import Footer
from ui.WelcomeScreen import WelcomeScreen
from ui.GithubCredentialsScreen import GitHubCredentialsScreen

class UI(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Hera Package Installer")
        self.geometry("600x550")
        self.resizable(False, False)

        self.sidebar = Sidebar(self)
        self.titlebar = Titlebar(self)
        self.footer = Footer(self, self)

        self.screens = {
            "welcome": lambda: WelcomeScreen(self),
            "github": lambda: GitHubCredentialsScreen(self),
        }
        self.screen_to_button_index = {
            "welcome": 0,
            "github": 1,
            # Add other screens and their corresponding button indexes here
        }
        self.created_screens = {}
        self.current_screen_name = None  # Variable to store the current screen name

        self.change_screen("welcome")

        self.sidebar.set_button_pressed(0)

    def change_screen(self, screen_name):
        if self.current_screen_name is not None and self.current_screen_name in self.created_screens:
            self.created_screens[self.current_screen_name].pack_forget()

        if screen_name not in self.created_screens:
            self.created_screens[screen_name] = self.screens[screen_name]()

        self.current_screen_name = screen_name  # Update current screen name
        self.current_screen = self.created_screens[screen_name]
        self.current_screen.pack(fill="both", expand=True)

        # Update the pressed button in the sidebar
        button_index = self.screen_to_button_index.get(screen_name, -1)
        if button_index != -1:
            self.sidebar.set_button_pressed(button_index)

    def run(self):
        self.mainloop()