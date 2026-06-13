from backend.utils.github_cloner import (
    GitHubCloner
)

from backend.graph.repository_loader import (
    RepositoryLoader
)

from backend.analysis.architecture_report import (
    ArchitectureReportGenerator
)

from backend.ai.repository_chat import (
    RepositoryChat
)

from config import GEMINI_API_KEY


URI = "bolt://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "Ynvdeepak@24"


repo_url = input(
    "Enter GitHub Repository URL: "
)

cloner = GitHubCloner()

repo_path = cloner.clone_repository(
    repo_url
)

loader = RepositoryLoader(
    URI,
    USERNAME,
    PASSWORD
)

graph = loader.load_repository(
    repo_path
)

generator = ArchitectureReportGenerator()

report = generator.generate(
    graph
)

chat = RepositoryChat()

print("\nRepository analyzed successfully.")

while True:

    question = input(
        "\nAsk a question (or quit): "
    )

    if question.lower() == "quit":
        break

    answer = chat.ask_question(
        str(report),
        question
    )

    print("\n")
    print(answer)