import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image

class UI(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("CTk Example")
        self.geometry("800x600")
        self.resizable(False, False)
        self._create_sidebar()
        self._create_main()
    
    def _create_sidebar(self):
        sidebar = ctk.CTkFrame(self)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(0)
        return sidebar

    def _create_main(self):
        main = ctk.CTkFrame(self)
        main.pack(side="right", fill="both", expand=True)
        main.pack_propagate(0)
        title = ctk.CTkLabel(main, text="CTk Example", font=("Arial", 20))
        title.pack(pady=10)
        text = ctk.CTkLabel(main, text="This is an example of how to use CTk")
        text.pack(pady=10)
        return main

    def run(self):
        self.mainloop()