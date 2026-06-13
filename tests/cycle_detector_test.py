from backend.graph.repository_loader import RepositoryLoader
from backend.analysis.cycle_detector import CycleDetector


URI = "bolt://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "Ynvdeepak@24"


loader = RepositoryLoader(
    URI,
    USERNAME,
    PASSWORD
)

graph = loader.load_repository("tests")

detector = CycleDetector()

has_cycle = detector.detect_cycles(graph)

print("\nCycle Detection Result\n")

print("Cycle Found:", has_cycle)