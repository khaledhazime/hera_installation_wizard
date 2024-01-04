import customtkinter as ctk
from ui.Colors import Colors


class WelcomeScreen(ctk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs, corner_radius=0)
        self.pack(fill="both", pady=0, padx=0, expand=True)
        self.configure(fg_color=Colors().palette["main_background"])

        self.welcome_text = "Welcome to the HERA Wizard!\nThis wizard will guide you through the installation of the HERA sofBGÓDREFtware.\nPlease follow the steps in the sidebar to complete the installation."

        self.title_label = ctk.CTkLabel(
            self,
            text=self.welcome_text,
            text_color="black",
            font=("Futura", 20, "bold"),
            wraplength=400,
        )
        self.title_label.pack(padx=10, pady=10, fill="both", expand=True)

        self.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        new_width = event.width
        self.title_label.configure(wraplength=new_width - 20)
