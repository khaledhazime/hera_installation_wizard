import ui as UI
import github as Github
import workspace as Workspace
import dependencies as Dependencies

class App():
    def __init__(self):
        self.ui = UI.UI()
        self.github = Github.Github()
        self.workspace = Workspace.Workspace()
        self.dependencies = Dependencies.Dependencies()
        self.ui.run()
        

if __name__ == "__main__":
    app = App()
    