import os


class RepositoryScanner:

    def scan_python_files(self, root_directory):

        python_files = []

        for root, dirs, files in os.walk(root_directory):

            for file in files:

                if file.endswith(".py"):
                    python_files.append(
                        os.path.join(root, file)
                    )

        return python_files