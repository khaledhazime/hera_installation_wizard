import customtkinter as ctk
from ui.Colors import Colors

class Footer(ctk.CTkFrame):
    def __init__(self, parent, ui_reference, *args, **kwargs):
        super().__init__(parent, *args, **kwargs, corner_radius=0)
        self.pack(side="bottom", fill="x", pady=0, padx=0)
        self.configure(fg_color=Colors().palette["titlebar_background"])

        self.cancel_button = ctk.CTkButton(
            self,
            text="Cancel",
            fg_color=Colors().palette["inactive_button_color"],
            hover_color=Colors().palette["active_button_color"],
            font=("Futura", 12, "bold"),
            width=120,
            height=30,
            text_color="black",
            command=self.on_cancel  # Assuming a cancel button functionality
        )
        self.cancel_button.pack(side="left", fill="x", padx=10, pady=10)

        self.back_button = ctk.CTkButton(
            self,
            text="Back",
            fg_color=Colors().palette["inactive_button_color"],
            hover_color=Colors().palette["active_button_color"],
            font=("Futura", 12, "bold"),
            width=120,
            height=30,
            text_color="black",
            # Replace with the actual screen you want to switch to
            command=lambda: ui_reference.change_screen("welcome")
        )
        self.back_button.pack(side="left", fill="x", padx=10, pady=10)

        self.next_button = ctk.CTkButton(
            self,
            text="Next",
            fg_color=Colors().palette["inactive_button_color"],
            hover_color=Colors().palette["active_button_color"],
            font=("Futura", 12, "bold"),
            width=120,
            height=30,
            text_color="black",
            # Replace with the actual screen you want to switch to
            command=lambda: ui_reference.change_screen("github")
        )
        self.next_button.pack(side="left", fill="x", padx=10, pady=10)

    def on_cancel(self):
        # Define what should happen when Cancel is pressed
        pass
