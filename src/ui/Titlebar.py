import customtkinter as ctk
from ui.Colors import Colors


class Titlebar(ctk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs, corner_radius=0)
        self.pack(side="top", fill="x", pady=0, padx=0)
        self.configure(fg_color=Colors().palette["titlebar_background"])

        self.title_label = ctk.CTkLabel(
            self, text="HERA Wizard", text_color="black", font=("Futura", 20, "bold")
        )
        self.title_label.pack(fill="x", padx=10, pady=10)
