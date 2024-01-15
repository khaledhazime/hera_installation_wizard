import customtkinter as ctk
from ui.Colors import Colors

class GitHubCredentialsScreen(ctk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs, corner_radius=0)
        self.pack(fill="both", pady=0, padx=0, expand=True)
        self.configure(fg_color=Colors().palette["main_background"])

        self.username = None
        self.token = None
        
        # Explanatory Text
        self.explanation_text = ("Enter your GitHub credentials\n"
                                "Please provide your GitHub username and a personal access token to proceed.\n\n "
                                "These credentials are necessary to access and manage your repositories.")

        self.explanation_label = ctk.CTkLabel(
            self,
            text=self.explanation_text,
            text_color="black",
            font=("Futura", 15),
            wraplength=400,
        )
        self.explanation_label.pack(padx=10, pady=10, expand=False, side="top")


        # GitHub Username Field
        self.username_label = ctk.CTkLabel(self, text="GitHub Username:", text_color="black", font=("Futura", 12))
        self.username_label.pack(padx=10, pady=(10, 2), anchor="w")
        self.username_entry = ctk.CTkEntry(self, width=380, placeholder_text="Enter your username")
        self.username_entry.pack(padx=10, pady=(0, 10))

        # GitHub Token Field
        self.token_label = ctk.CTkLabel(self, text="GitHub Token:", text_color="black", font=("Futura", 12))
        self.token_label.pack(padx=10, pady=(10, 2), anchor="w")
        self.token_entry = ctk.CTkEntry(self, width=380, placeholder_text="Enter your personal access token")
        self.token_entry.pack(padx=10, pady=(0, 10))
        self.token_help_label = ctk.CTkLabel(
            self,
            text="Click here to learn how to generate a personal access token",
            text_color="blue",
            font=("Futura", 10),
            cursor="hand2",
        )
        self.token_help_label.pack(padx=10, pady=(0, 10), anchor="w")
        self.token_help_label.bind("<Button-1>", lambda e: self.open_token_help())

        self.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        new_width = event.width
        self.explanation_label.configure(wraplength=new_width - 20)

    def are_credentials_filled(self):
        return bool(self.username_entry.get()) and bool(self.token_entry.get())
    
    def open_token_help(self):
        import webbrowser
        webbrowser.open("https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token")
    
