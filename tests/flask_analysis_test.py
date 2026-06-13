from backend.graph.repository_loader import RepositoryLoader
from backend.analysis.architecture_report import (
    ArchitectureReportGenerator
)

URI = "bolt://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "Ynvdeepak@24"

loader = RepositoryLoader(
    URI,
    USERNAME,
    PASSWORD
)

graph = loader.load_repository(
    "repositories/flask/src/flask"
)

generator = ArchitectureReportGenerator()

report = generator.generate(graph)

print("\n")
print("=" * 50)
print("FLASK ARCHITECTURE REPORT")
print("=" * 50)

for key, value in report.items():
    print(f"{key}: {value}")

print("=" * 50)