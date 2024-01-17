import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from ui.Colors import Colors
import json
import os

class PackageCustomization(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Customize Packages")
        self.geometry("800x500")
        # Start window hidden
        self.withdraw()
        
        self.package_data = self.load_data_from_json(default = False)
        self.package_names = [package["name"] for package in self.package_data]

    def show(self):
        # Create window
        self.deiconify()
        self.create_widgets()

    def create_widgets(self):
        if hasattr(self, "tree"):
            return
            
        self.tree = ttk.Treeview(self, columns=("Repository", "Organization", "Branch"), show='headings', selectmode="browse")
        self.tree.heading("Repository", text="Repository")
        self.tree.heading("Organization", text="Organization")
        self.tree.heading("Branch", text="Branch")
        self.tree.column("Repository", anchor=tk.W, width=120)
        self.tree.column("Organization", anchor=tk.W, width=120)
        self.tree.column("Branch", anchor=tk.W, width=120)
        self.tree.bind("<Double-1>", self.on_double_click)

        for package in self.package_data:
            self.tree.insert("", tk.END, values=(package["name"], package["organization"], package["selected_branch"]))

        # Add Scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Buttons
        exit_button = ctk.CTkButton(self, text="Exit", command=self.exit)
        exit_button.pack(side=tk.BOTTOM, pady=10)
        save_button = ctk.CTkButton(self, text="Save", command=self.save_data_to_json)
        save_button.pack(side=tk.BOTTOM, pady=10)
        load_default_button = ctk.CTkButton(self, text="Load Default", command=self.load_default_data)
        load_default_button.pack(side=tk.BOTTOM, pady=10)
        remove_button = ctk.CTkButton(self, text="Remove Package", command=None)
        remove_button.pack(side=tk.BOTTOM, pady=10)
        add_button = ctk.CTkButton(self, text="Add Package", command=self.add_new_row)
        add_button.pack(side=tk.BOTTOM, pady=10)
    
    def on_double_click(self, event):
        item = self.tree.selection()[0]
        column = self.tree.identify_column(event.x)
        
        # Convert the column number to an index (e.g., '#1' to 0, '#2' to 1)
        col_index = int(column.replace('#', '')) - 1

        # Check if the clicked column is not 'Branch'
        if col_index != 2:  # Assuming 'Branch' is the third column
            self.make_cell_editable(item, column)
        else:
            self.edit_branches(item, column)

    def make_cell_editable(self, item, column):
        x, y, width, height = self.tree.bbox(item, column)
        
        # Create an Entry widget
        entry = tk.Entry(self, width=width)
        entry.place(x=x, y=y, width=width, height=height)

        entry.insert(0, self.tree.set(item, column))
        entry.focus()

        # Save on Enter key, and destroy Entry widget on focus out
        entry.bind('<Return>', lambda e: self.save_edit(item, column, entry.get()))
        entry.bind('<FocusOut>', lambda e: entry.destroy())
        
    def add_new_row(self):
        new_item = self.tree.insert("", tk.END, values=("", "", ""))

        # Optionally, automatically make this new row editable
        self.make_row_editable(new_item)
    
    def make_row_editable(self, item):
        # Assuming there are three columns: 'Repository', 'Organization', 'Branch'
        for col in ['Branch', 'Organization', 'Repository']:
            self.create_editable_cell(item, col)

    def create_editable_cell(self, item, column):
        x, y, width, height = self.tree.bbox(item, column)

        # Create an Entry widget
        self.entry = tk.Entry(self, width=width)
        self.entry.place(x=x, y=y, width=width, height=height)

        self.entry.insert(0, self.tree.set(item, column))
        self.entry.focus()

        # Save on Enter key, and destroy Entry widget on focus out
        self.entry.bind('<Return>', lambda e: self.save_edit(item, column, self.entry.get()))
        
        

    def save_edit(self, item, column, value):
        # Update Treeview
        self.tree.set(item, column, value)

        # Update package_data
        package_name = self.tree.item(item, 'values')[0]
        for package in self.package_data:
            if package["name"] == package_name:
                package[column.lower()] = value  # Update the relevant field

        # Destroy all Entry widgets (cleanup)
        for child in self.winfo_children():
            if isinstance(child, tk.Entry):
                child.destroy()
    
    def edit_branches(self, item, column):
        # Get the bounding box of the cell
        x, y, width, height = self.tree.bbox(item, column)

        # Find the package data for the selected item
        package_name = self.tree.item(item, 'values')[0]
        package = next((pkg for pkg in self.package_data if pkg["name"] == package_name), None)
        if not package:
            return  # Package not found

        # Create a Combobox
        self.combo_branches = ttk.Combobox(self, values=package["branches"])
        self.combo_branches.place(x=x, y=y, width=width, height=height)

        # Set the current value of the combobox
        self.combo_branches.set(package["selected_branch"])

        # Focus on the Combobox
        self.combo_branches.focus()

        # Bind selection event to save the edited value
        self.combo_branches.bind("<<ComboboxSelected>>", lambda e: self.save_branch_edit(item, column))
        
    def save_branch_edit(self, item, column):
        # Check if the Combobox still exists
        if self.combo_branches:
            selected_branch = self.combo_branches.get()

            # Update the treeview item and the package data with the selected branch
            self.tree.set(item, column, selected_branch)

            package_name = self.tree.item(item, 'values')[0]
            package = next((pkg for pkg in self.package_data if pkg["name"] == package_name), None)
            if package:
                package["selected_branch"] = selected_branch

            # Destroy the Combobox
            self.combo_branches.destroy()
            self.combo_branches = None  # Reset the attribute to None
            self.print_package_data()
    
    def print_package_data(self):
        for package in self.package_data:
            print(package)
            
    def save_data_to_json(self):
        # Save the package data to a JSON file
        relative_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'package_data.json')
        absolute_path = os.path.abspath(relative_path)

        with open(absolute_path, 'w') as file:
            json.dump(self.package_data, file, indent=4)
    
    def load_data_from_json(self, default):
        try:
            if default:
                relative_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'default_package_data.json')
            else:
                relative_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'package_data.json')
            absolute_path = os.path.abspath(relative_path)

            with open(absolute_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading JSON data: {e}")
            return []

    def load_default_data(self):
        self.package_data = self.load_data_from_json(default = True)
        self.package_names = [package["name"] for package in self.package_data]
        self.tree.delete(*self.tree.get_children())
        for package in self.package_data:
            self.tree.insert("", tk.END, values=(package["name"], package["organization"], package["selected_branch"]))
    
    def exit(self):
        self.withdraw()

    def add_package_window(self):
        # Create a new CustomTkinter top-level window
        add_window = ctk.CTkToplevel(self)
        add_window.title("Add New Package")
        add_window.geometry("300x200")

        # Name field
        ctk.CTkLabel(add_window, text="Name:").pack(pady=(10, 0))
        name_entry = ctk.CTkEntry(add_window)
        name_entry.pack()

        # Organization field
        ctk.CTkLabel(add_window, text="Organization:").pack(pady=(10, 0))
        org_entry = ctk.CTkEntry(add_window)
        org_entry.pack()

        # Branch field
        ctk.CTkLabel(add_window, text="Branch:").pack(pady=(10, 0))
        branch_entry = ctk.CTkEntry(add_window)
        branch_entry.pack()

        # Add Button
        add_btn = ctk.CTkButton(add_window, text="Add", command=lambda: self.add_new_package(name_entry.get(), org_entry.get(), branch_entry.get(), add_window))
        add_btn.pack(pady=(10, 0))
    
    def add_new_package(self, name, organization, branch, add_window):
        # Validate input
        if not name or not organization or not branch:
            tk.messagebox.showerror("Error", "All fields are required.")
            return

        # Add the new package to package_data
        new_package = {
            "name": name,
            "organization": organization,
            "branches": [branch],
            "selected_branch": branch
        }
        self.package_data.append(new_package)

        # Add the new package to the Treeview
        self.tree.insert("", tk.END, values=(name, organization, branch))

        # Close the add window
        add_window.destroy()

        # Optionally, print the package data to the console
        self.print_package_data()