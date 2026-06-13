
from parser.python_parser import PythonParser
from parser.repository_scanner import RepositoryScanner
from graph.repository_graph import RepositoryGraph


scanner = RepositoryScanner()
parser = PythonParser()

files = scanner.scan_python_files("tests")

parsed_results = []

for file in files:

    result = parser.parse_file(file)

    parsed_results.append(result)

repository_graph = RepositoryGraph()

graph = repository_graph.build_repository_graph(
    parsed_results
)

print("\nRepository Knowledge Graph:\n")

for source, targets in graph.items():

    if not targets:
        print(source)

    for target in targets:
        print(f"{source} ---> {target}")