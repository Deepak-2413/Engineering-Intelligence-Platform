from backend.graph.repository_loader import RepositoryLoader


URI = "bolt://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "Ynvdeepak@24"


loader = RepositoryLoader(
    URI,
    USERNAME,
    PASSWORD
)

graph = loader.load_repository("tests")

print(graph)