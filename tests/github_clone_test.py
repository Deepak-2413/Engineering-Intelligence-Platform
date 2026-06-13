from backend.utils.github_cloner import (
    GitHubCloner
)

cloner = GitHubCloner()

path = cloner.clone_repository(
    "https://github.com/pallets/flask.git"
)

print("Repository Cloned To:")
print(path)