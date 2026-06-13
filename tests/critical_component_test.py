from backend.graph.repository_loader import RepositoryLoader
from backend.analysis.critical_component import (
    CriticalComponentAnalyzer
)


URI = "bolt://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "Ynvdeepak@24"


loader = RepositoryLoader(
    URI,
    USERNAME,
    PASSWORD
)

graph = loader.load_repository("tests")

analyzer = CriticalComponentAnalyzer()

critical = analyzer.find_critical_components(
    graph
)

print("\nCritical Components Ranking\n")

for component, score in critical:
    print(f"{component}: {score}")