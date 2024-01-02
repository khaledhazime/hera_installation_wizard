import json
import subprocess

class DependencyManagerError(Exception):
    """Exception raised for errors in dependency management or installation."""
    pass

class DependencyManager:
    def __init__(self, dependencies_file="assets/dependencies.json"):
        self.dependencies_file = dependencies_file
        self.load_dependencies()

    def load_dependencies(self):
        try:
            with open(self.dependencies_file, 'r') as file:
                self.dependencies = json.load(file)
        except FileNotFoundError:
            self.dependencies = {"ros": [], "python": [], "system": []}
            self.save_dependencies()
        except json.JSONDecodeError:
            raise DependencyManagerError("Error parsing dependencies file.")

    def save_dependencies(self):
        with open(self.dependencies_file, 'w') as file:
            json.dump(self.dependencies, file, indent=4)

    def add_dependency(self, category, dependency):
        if dependency not in self.dependencies[category]:
            self.dependencies[category].append(dependency)
            self.save_dependencies()

    def remove_dependency(self, category, dependency):
        if dependency in self.dependencies[category]:
            self.dependencies[category].remove(dependency)
            self.save_dependencies()

    def edit_dependency(self, category, old_dependency, new_dependency):
        if old_dependency in self.dependencies[category]:
            index = self.dependencies[category].index(old_dependency)
            self.dependencies[category][index] = new_dependency
            self.save_dependencies()

    def install_dependencies(self, category):
        for dep in self.dependencies[category]:
            try:
                print(f"Installing {category} dependency: {dep}...")
                if category == "ros" or category == "system":
                    subprocess.run(["sudo", "apt-get", "install", "-y", dep], check=True)
                elif category == "python":
                    subprocess.run(["pip", "install", dep], check=True)
                print(f"Successfully installed {dep}")
            except subprocess.CalledProcessError:
                raise DependencyManagerError(f"Failed to install {dep}")