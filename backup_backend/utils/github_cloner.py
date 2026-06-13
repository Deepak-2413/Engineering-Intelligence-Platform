import os
import tempfile

from git import Repo


class GitHubCloner:

    def clone_repository(
        self,
        repo_url,
        target_folder="repositories"
    ):

        os.makedirs(
            target_folder,
            exist_ok=True
        )

        repo_name = repo_url.split("/")[-1]

        if repo_name.endswith(".git"):
            repo_name = repo_name[:-4]

        local_path = os.path.join(
            target_folder,
            repo_name
        )

        if not os.path.exists(local_path):

            Repo.clone_from(
                repo_url,
                local_path
            )

        return local_path

    def clone_branch(
        self,
        repo_url,
        branch_name
    ):

        temp_dir = tempfile.mkdtemp()

        Repo.clone_from(
            repo_url,
            temp_dir,
            branch=branch_name
        )

        return temp_dir