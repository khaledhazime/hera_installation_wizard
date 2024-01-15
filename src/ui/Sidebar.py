import customtkinter as ctk
from PIL import Image, ImageTk
from ui.Colors import Colors

class Sidebar(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, corner_radius=0)
        self.colors = Colors()
        self.pack(side="left", fill="y", padx=0, pady=0)

        self.configure(fg_color=self.colors.palette["sidebar_background"])
        # self.pack_propagate(0)  # Prevents the frame from shrinking to the size of its contents

        # Load and display the image
        self.load_resized_image("assets/hera.png", 200, 200)

        self.buttons = []
        self._create_buttons()

    def load_resized_image(self, image_path, width, height):
        image = Image.open(image_path)
        image.thumbnail((width, height), Image.ANTIALIAS)  # Better thumbnail scaling
        self.image = ImageTk.PhotoImage(image)
        image_label = ctk.CTkLabel(self, image=self.image)
        image_label.pack(pady=20)  # Increased padding for better spacing

    def add_button(self, text):
        button = ctk.CTkButton(
            self,
            text=text,
            text_color_disabled="black",
            width=200,  # Increased width for better fit
            height=40,  # Increased height for better clickability
            font=("Futura", 12, "bold"),
            corner_radius=5,  # Added slight corner radius for a modern look
            anchor="w",
        )
        button.pack(pady=5)  # Reduced padding for tighter layout
        self.buttons.append(button)
        return button

    def _create_buttons(self):
        button_titles = ["Welcome", "Github Credentials", "Workspace setup", "Dependencies", "Installation", "Exit"]
        for title in button_titles:
            self.add_button(title)

    def set_button_pressed(self, index):
        for idx, button in enumerate(self.buttons):
            if idx == index:
                button.configure(
                    fg_color=self.colors.palette["main_background"],
                    text_color_disabled="black",
                    font=("Futura", 12, "bold"),
                    state="disabled",
                )
            else:
                button.configure(
                    fg_color=self.colors.palette["sidebar_background"],
                    hover_color=self.colors.palette["inactive_button_color"],  # Adjusted for clarity
                    text_color_disabled="black",
                    font=("Futura", 12, "bold"),
                    state="disabled",
                )
