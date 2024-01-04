import ui.main as UI
import core.Github as Github
import core.Workspace as Workspace
import core.Dependencies as Dependencies

class App():
    def __init__(self):
        self.ui = UI.UI()
        self.github = Github.Github()
        self.workspace = Workspace.Workspace()
        self.dependencies = Dependencies.DependencyManager()
        self.ui.run()
        

if __name__ == "__main__":
    app = App()
    