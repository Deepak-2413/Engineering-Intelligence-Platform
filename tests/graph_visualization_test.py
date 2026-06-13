from backend.graph.repository_loader import (
    RepositoryLoader
)

from backend.visualization.graph_visualizer import (
    GraphVisualizer
)


loader = RepositoryLoader()

graph = loader.load_repository(
    "repositories/flask"
)

visualizer = GraphVisualizer()

output = visualizer.generate_graph(
    graph
)

print(
    "Graph Generated:",
    output
)