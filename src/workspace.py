import os
import shutil

class PathError(Exception):
    """Exception raised when the path is invalid."""
    pass

class CreationError(Exception):
    """Exception raised when creating the workspace fails."""
    pass

class DeletionError(Exception):
    """Exception raised when deleting the workspace fails."""
    pass

class Workspace():
    def __init__(self, path):
        self.set_path(path)
    
    def set_path(self, path):
        expanded_path = os.path.expanduser(path)
        if not os.path.isabs(expanded_path):
            raise PathError("Path must be an absolute path")
        if not os.path.isdir(os.path.dirname(expanded_path)):
            raise PathError("Parent directory of the path does not exist")
        self.path = expanded_path
    
    def create_workspace(self):
        if os.path.exists(self.path):
            print(f"Workspace already exists at {self.path}")
            return False
        else:
            try:
                os.makedirs(self.path)
            except OSError as e:
                raise CreationError(f"Error creating workspace: {e}")

    def delete_workspace(self, confirm=False):
        if not confirm:
            raise DeletionError("Deletion confirmation not provided")
        if not os.path.exists(self.path):
            raise DeletionError("Workspace does not exist")
        try:
            shutil.rmtree(self.path)
        except OSError as e:
            raise DeletionError(f"Error deleting workspace: {e}")

    def list_contents(self):
        if not os.path.exists(self.path):
            raise FileNotFoundError("Workspace does not exist")
        try:
            return os.listdir(self.path)
        except OSError as e:
            raise IOError(f"Error listing contents: {e}")

    def __str__(self):
        return f"Workspace Path: {self.path}"