import customtkinter as ctk
from ui.Colors import Colors


class WorkspaceSetup(ctk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs, corner_radius=0)
        self.pack(fill="both", pady=0, padx=0, expand=True)
        self.configure(fg_color=Colors().palette["main_background"])

        self.workspace_path = "~/Workspace/hera_ws"
        self.folder_setup()
        self.packages_selection()

    def folder_setup(self):
        self.explanation_text = ctk.CTkLabel(
            self,
            text="Enter your desired workspace path",
            text_color="black",
            font=("Futura", 15),
            wraplength=400,
        )
        self.explanation_text.pack(padx=10, pady=10, expand=False, side="top")

        # Inner frame for entry and button
        self.entry_frame = ctk.CTkFrame(self)
        self.entry_frame.pack(padx=10, pady=(0, 10), fill="x")
        self.entry_frame.configure(fg_color=Colors().palette["main_background"])

        # Workspace path entry
        self.workspace_path_entry = ctk.CTkEntry(
            self.entry_frame,
            width=320,
            placeholder_text="Select your desired workspace path",
        )
        self.workspace_path_entry.pack(side="left", expand=True, fill="x")
        self.workspace_path_entry.insert(0, self.workspace_path)
        self.workspace_path_entry.configure(state="readonly")

        # Browse button
        self.browse_button = ctk.CTkButton(
            self.entry_frame, text="Browse", command=self.browse_folder
        )
        self.browse_button.pack(side="right")

    def browse_folder(self):
        folder_selected = ctk.filedialog.askdirectory()
        if folder_selected:
            self.workspace_path_entry.configure(state="normal")
            self.workspace_path_entry.delete(0, "end")
            self.workspace_path_entry.insert(0, folder_selected)
            self.workspace_path_entry.configure(state="readonly")
            self.workspace_path = folder_selected

    def packages_selection(self):
        self.explanation_text = ctk.CTkLabel(
            self,
            text="Select the packages you want to install",
            text_color="black",
            font=("Futura", 15),
            wraplength=400,
        )
        self.explanation_text.pack(padx=10, pady=10, expand=False, side="top")
        self.packages_frame = ctk.CTkFrame(self)
        
        self.packages_frame.pack(padx=10, pady=10, fill="both", expand=True)
        self.packages_frame.configure(fg_color=Colors().palette["main_background"])

        package_list = ['hera_bringup', 'hera_control', 'hera_hw', 'hera_nav',
                        'hera_simulation', 'hera_description', 'hera_objects', 'hera_speech',
                        'hera_face', 'track_flow', 'detector_2d']

        self.package_checkboxes = {}
        for i, package in enumerate(package_list):
            self.package_checkboxes[package] = ctk.CTkCheckBox(
                self.packages_frame, 
                text=package,
                text_color="black",
                font=("Futura", 12, 'bold')
            )
            row = i // 2  # Calculate row number (0-indexed)
            column = i % 2  # Calculate column number (0-indexed)
            if column == 0:
                self.package_checkboxes[package].grid(row=row, column=column, sticky="w", padx=(0, 10), pady=8)
            else:
                self.package_checkboxes[package].grid(row=row, column=column, sticky="ew", padx=(10, 0), pady=8)
        
        self.select_all_button = ctk.CTkButton(
            self,
            text="Select All",
            fg_color=Colors().palette["inactive_button_color"],
            hover_color=Colors().palette["active_button_color"],
            font=("Futura", 12, "bold"),
            width=120,
            height=30,
            text_color="black",
            command=None
        )
        self.select_all_button.pack(side="left", fill="x", padx=10, pady=10)
        self.customize_button = ctk.CTkButton(
            self,
            text="Customize",
            fg_color=Colors().palette["inactive_button_color"],
            hover_color=Colors().palette["active_button_color"],
            font=("Futura", 12, "bold"),
            width=120,
            height=30,
            text_color="black",
            command=None
        )
        self.customize_button.pack(side="left", fill="x", padx=10, pady=10)
        
        self.dropdown_frame = ctk.CTkFrame(
            self,
            width=120,
            height=30
        )
        self.dropdown_frame.pack(side="left", padx=10, pady=10)
        options = ["Sim", "Physical", "Both"]
        self.dropdown_menu = ctk.CTkOptionMenu(
            self.dropdown_frame,
            values=options,
            text_color="black",
            font=("Futura", 12, "bold"),
            button_color=Colors().palette["active_button_color"],
            bg_color=Colors().palette["main_background"],
            dropdown_fg_color=Colors().palette["main_background"],
            fg_color=Colors().palette["active_button_color"],
            
        )
        self.dropdown_menu.pack(expand=True, fill="both")


    def get_workspace_path(self):
        return self.workspace_path
