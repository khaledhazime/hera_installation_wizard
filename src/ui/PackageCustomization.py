import customtkinter as ctk
from ui.Colors import Colors

class PackageCustomization(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # Set as hidden
        self.withdraw()
        self.package_data = [
            {"name": "hera_bringup", "organization": "robofeiathome", "branches": ["master", "dev"], "selected_branch" : "main"},
            {"name": "hera_description", "organization": "robofeiathome", "branches": ["master", "dev"], "selected_branch" : "main"},
            {"name": "hera_hw", "organization": "robofeiathome", "branches": ["master", "dev"], "selected_branch" : "main"},
            {"name": "hera_nav", "organization": "robofeiathome", "branches": ["master", "dev"], "selected_branch" : "main"},
            {"name": "hera_simulation", "organization": "robofeiathome", "branches": ["master", "dev"], "selected_branch" : "main"},
            {"name": "hera_control", "organization": "robofeiathome", "branches": ["master", "dev"], "selected_branch" : "main"},
            {"name": "hera_objects", "organization": "robofeiathome", "branches": ["master", "dev"], "selected_branch" : "main"},
            {"name": "hera_speech", "organization": "robofeiathome", "branches": ["master", "dev"], "selected_branch" : "main"},
            {"name": "hera_face", "organization": "robofeiathome", "branches": ["master", "dev"], "selected_branch" : "main"},
            {"name": "track_flow", "organization": "robofeiathome", "branches": ["master", "dev"], "selected_branch" : "main"},
            {"name": "detector_2d", "organization": "robofeiathome", "branches": ["master", "dev"], "selected_branch" : "main"},
            {"name": "hera_tasks", "organization": "robofeiathome", "branches": ["master", "dev"], "selected_branch" : "main"},
        ]
        self.package_names = [package['name'] for package in self.package_data]
    
    def show(self):
        self.create_widgets()
        # show window again
        self.deiconify()
        self.mainloop()

    def create_widgets(self):
        # Create headers for the table
        headers = ["Package Name", "Organization", "Branches", "Edit", "Remove"]
        for i, header in enumerate(headers):
            header_label = ctk.CTkLabel(self, text=header, font=("Futura", 12, 'bold'))
            header_label.grid(row=0, column=i, padx=10, pady=10, sticky="w")

        # Display packages in a table-like structure
        for i, package in enumerate(self.package_data, start=1):
            # Package name and organization labels
            name_label = ctk.CTkLabel(self, text=package['name'])
            name_label.grid(row=i, column=0, sticky="w")
            org_label = ctk.CTkLabel(self, text=package['organization'])
            org_label.grid(row=i, column=1, sticky="w")

            # Dropdown menu for branches
            branch_dropdown = ctk.CTkOptionMenu(self, values=package['branches'])
            branch_dropdown.grid(row=i, column=2, padx=5)

            # Edit and Remove buttons
            edit_button = ctk.CTkButton(self, text="Edit", command=lambda p=package['name']: self.edit_package(p))
            edit_button.grid(row=i, column=3, padx=5)
            remove_button = ctk.CTkButton(self, text="Remove", command=lambda p=package['name']: self.remove_package(p))
            remove_button.grid(row=i, column=4, padx=5)

        # Add package button
        add_button = ctk.CTkButton(self, text="Add Package", command=self.add_package)
        add_button.grid(row=len(self.package_data) + 1, column=0, columnspan=5, pady=10)

    def edit_package(self, package):
        # Implement package editing logic
        pass

    def remove_package(self, package):
        # Implement package removal logic
        
        pass

    def add_package(self):
        # Implement package addition logic
        pass