import customtkinter as ctk
from ui.Colors import Colors


class WelcomeScreen(ctk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs, corner_radius=0)
        self.pack(fill="both", pady=0, padx=0, expand=True)
        self.configure(fg_color=Colors().palette["main_background"])

        self.welcome_text = "Welcome to the HERA Wizard! \n"\
                            "This user-friendly setup will guide you through the installation or update of HERA packages, "\
                            "ensuring your computer is equipped with the latest packages.\n"\
                            "Simply enter your GitHub credentials to access and customize your package selection.\n"\
        
        self.next_label = "Please, click \"Next\" to continue."

        self.title_label = ctk.CTkLabel(
            self,
            text=self.welcome_text,
            text_color="black",
            font=("Futura", 15),
            wraplength=400,
        )
        self.title_label.pack(padx=10, pady=10, expand=False, side="top", anchor="w")
        
        self.next_label = ctk.CTkLabel(
            self,
            text=self.next_label,
            text_color="black",
            font=("Futura", 15),
            wraplength=400,
        )
        self.next_label.pack(padx=10, pady=10, expand=False, side="bottom")
        

        self.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        new_width = event.width
        self.title_label.configure(wraplength=new_width - 20)
