import requests
from requests.auth import HTTPBasicAuth
import subprocess


class Github:
    def __init__(self, username="", token="", selected_repos=[]):
        self.username = username
        self.token = token
        self.selected_repos = selected_repos
        self.repo_list = [
            "hera",
            "hera_face",
            "track_flow",
            "detector_2d",
            "hera_objects",
            "hera_nav",
            "hera_hw",
            "hera_control",
            "hera_speech",
        ]

    def verify_credentials(self):
        url = "https://api.github.com/user"
        response = requests.get(url, auth=HTTPBasicAuth(self.username, self.token))

        if response.status_code == 200:
            print("Authentication successful")
            return True
        else:
            print("Authentication failed")
            return False

    def get_branches_from_single_repo(self, repo):
        # Get branches from repo
        url = f"https://api.github.com/repos/{self.username}/{repo}/branches"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)
        branches = []
        for branch in response.json():
            branches.append(branch["name"])
        return branches

    def get_branches_from_all_repos(self):
        # Get branches from all repos and store in a dictionary
        branches = {}
        for repo in self.repo_list:
            branches[repo] = self.get_branches_from_single_repo(repo)
        return branches

    def clone_repos(self):
        # Ensure authentication is successful before proceeding
        if not self.verify_credentials():
            print("Cannot clone repositories due to failed authentication.")
            return

        for repo in self.selected_repos:
            # Construct the clone URL
            clone_url = f"https://{self.username}:{self.token}@github.com/robofeiathome/{repo}.git"

            # Run the git clone command
            try:
                print(f"Cloning repository: {repo}")
                subprocess.run(["git", "clone", clone_url], check=True)
                print(f"Successfully cloned {repo}")
            except subprocess.CalledProcessError:
                print(f"Failed to clone repository: {repo}")

    def __str__(self):
        return f"Username: {self.username}\nToken: {self.token}\nRepo List: {self.repo_list}"
