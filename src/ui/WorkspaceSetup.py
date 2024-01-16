import customtkinter as ctk
from ui.Colors import Colors


class WorkspaceSetup(ctk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs, corner_radius=0)
        self.pack(fill="both", pady=0, padx=0, expand=True)
        self.configure(fg_color=Colors().palette["main_background"])
        self.all_selected = False

        self.workspace_path = "~/Workspace/hera_ws"
        self.selected_packages = []
        
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

        package_list = ['hera_bringup', 'hera_description', 'hera_hw', 'hera_nav',
                        'hera_simulation', 'hera_control', 'hera_objects', 'hera_speech',
                        'hera_face', 'track_flow', 'detector_2d', 'hera_tasks']

        # Determine the number of columns (2 or 3) based on the number of packages
        num_columns = 3 if len(package_list) >= 12 else 2

        self.package_checkboxes = {}
        for i, package in enumerate(package_list):
            self.package_checkboxes[package] = ctk.CTkCheckBox(
                self.packages_frame, 
                text=package,
                text_color="black",
                font=("Futura", 12, 'bold'),
                command=lambda p=package: self.handle_checkbox(p)
            )
            row = i // num_columns  # Calculate row number (0-indexed)
            column = i % num_columns  # Calculate column number (0-indexed)

            # Adjust padding based on the position
            if column == 0:
                padx = (0, 0)
            elif column == num_columns - 1:
                padx = (5, 0)
            else:
                padx = (5, 5)

            self.package_checkboxes[package].grid(row=row, column=column, sticky="w", padx=padx, pady=8)

        
        self.select_all_button = ctk.CTkButton(
            self,
            text="Select All",
            fg_color=Colors().palette["inactive_button_color"],
            hover_color=Colors().palette["active_button_color"],
            font=("Futura", 12, "bold"),
            width=120,
            height=30,
            text_color="black",
            command=self.select_all_handler
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
            command=self.customize_packages
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

    def select_all_handler(self):
        if not self.all_selected:
            # Select all checkboxes
            for checkbox in self.package_checkboxes.values():
                checkbox.select()
                self.selected_packages = list(self.package_checkboxes.keys())  # Add all packages
            self.select_all_button.configure(text="Unselect All")
            self.all_selected = True
        else:
            # Deselect all checkboxes
            for checkbox in self.package_checkboxes.values():
                checkbox.deselect()
                self.selected_packages.clear()  # Clear the list
            self.select_all_button.configure(text="Select All")
            self.all_selected = False

    def handle_checkbox(self, package):
        checkbox = self.package_checkboxes[package]
        if checkbox.get() == 1:  # Checkbox is checked
            if package not in self.selected_packages:
                self.selected_packages.append(package)
        else:  # Checkbox is unchecked
            if package in self.selected_packages:
                self.selected_packages.remove(package)

        # Check if all checkboxes are selected
        self.all_selected = all(checkbox.get() == 1 for checkbox in self.package_checkboxes.values())
        self.select_all_button.configure(text="Unselect All" if self.all_selected else "Select All")
        print('Selected packages:' + str(self.selected_packages))

    def get_workspace_path(self):
        return self.workspace_path
    
    def customize_packages(self):
        self.customize_window = ctk.CTkToplevel(self)
        self.customize_window.title("Customize Packages")
        self.customize_window.geometry("600x400")  # Adjust size as needed

        # Example package data as a list of dictionaries
        self.package_data = [
            {"name": "hera_bringup", "organization": "example_org", "branches": ["main", "dev"]},
            # ... [other packages] ...
        ]

        # Create headers for the table
        headers = ["Package Name", "Organization", "Branches", "Edit", "Remove"]
        for i, header in enumerate(headers):
            header_label = ctk.CTkLabel(self.customize_window, text=header, font=("Futura", 12, 'bold'))
            header_label.grid(row=0, column=i, padx=10, pady=10, sticky="w")

        # Display packages in a table-like structure
        for i, package in enumerate(self.package_data, start=1):  # Start from row 1 to leave space for headers
            # Package name and organization labels
            name_label = ctk.CTkLabel(self.customize_window, text=package['name'])
            name_label.grid(row=i, column=0, sticky="w")
            org_label = ctk.CTkLabel(self.customize_window, text=package['organization'])
            org_label.grid(row=i, column=1, sticky="w")

            # Dropdown menu for branches
            branch_dropdown = ctk.CTkOptionMenu(self.customize_window, values=package['branches'])
            branch_dropdown.grid(row=i, column=2, padx=5)

            # Edit and Remove buttons
            edit_button = ctk.CTkButton(self.customize_window, text="Edit", command=lambda p=package['name']: self.edit_package(p))
            edit_button.grid(row=i, column=3, padx=5)
            remove_button = ctk.CTkButton(self.customize_window, text="Remove", command=lambda p=package['name']: self.remove_package(p))
            remove_button.grid(row=i, column=4, padx=5)

        # Add package button
        add_button = ctk.CTkButton(self.customize_window, text="Add Package", command=self.add_package)
        add_button.grid(row=len(self.package_data) + 1, column=0, columnspan=5, pady=10)
