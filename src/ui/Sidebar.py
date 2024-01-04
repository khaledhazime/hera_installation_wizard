import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import Tk
from ui.Colors import Colors

class Sidebar(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, corner_radius=0)
        self.colors = Colors()
        self.pack(side="left", fill="y", padx=0, pady=0)  # ipadx sets the internal padding, adjusting the width

        self.configure(fg_color=self.colors.palette["sidebar_background"])
        self.pack_propagate(0)

        self.load_resized_image("assets/hera.png", 300, 300)

        self.buttons = []
        self._create_buttons()

    def load_resized_image(self, image_path, width, height):
        image = Image.open(image_path)
        aspect_ratio = image.width / image.height
        new_width = min(width, int(height * aspect_ratio))
        new_height = min(height, int(width / aspect_ratio))
        image = image.resize((new_width, new_height), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(image)
        image_label = ctk.CTkLabel(self, image=self.image, width=new_width, height=new_height, text="")
        image_label.pack(pady=10)

    def add_button(self, text):
        button = ctk.CTkButton(self, text=text, state="disabled", fg_color="gray", hover_color="gray", text_color_disabled="black", width=180, height=30, font=("Futura", 12, "bold"))
        button.pack(pady=1)
        self.buttons.append(button)
        return button

    def _create_buttons(self):
        self.add_button("Welcome")
        self.add_button("Github Credentials")
        self.add_button("Workspace setup")
        self.add_button("Dependencies")
        self.add_button("Installation")
        self.add_button("Exit")

    def set_button_pressed(self, index):
        for idx, button in enumerate(self.buttons):
            if idx == index:
                button.configure(fg_color=self.colors.palette["active_button_color"], hover_color=self.colors.palette["active_button_color"], text_color_disabled="black", font=("Futura", 12, "bold"))
            else:
                button.configure(fg_color=self.colors.palette["inactive_button_color"], hover_color=self.colors.palette["inactive_button_color"], text_color_disabled="black", font=("Futura", 12, "bold"))