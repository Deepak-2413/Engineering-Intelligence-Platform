from backend.graph.repository_loader import RepositoryLoader
from backend.analysis.repository_health import RepositoryHealthAnalyzer


URI = "bolt://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "Ynvdeepak@24"


loader = RepositoryLoader(
    URI,
    USERNAME,
    PASSWORD
)

graph = loader.load_repository("tests")

analyzer = RepositoryHealthAnalyzer()

report = analyzer.analyze(graph)

print("\nRepository Health Report\n")

for key, value in report.items():
    print(f"{key}: {value}")