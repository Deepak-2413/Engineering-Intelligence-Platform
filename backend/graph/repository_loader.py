from backend.parser.repository_scanner import RepositoryScanner
from backend.parser.python_parser import PythonParser
from backend.graph.repository_graph import RepositoryGraph
from backend.graph.neo4j_manager import Neo4jManager


class RepositoryLoader:

    def __init__(
        self,
        uri=None,
        username=None,
        password=None
    ):

        self.scanner = RepositoryScanner()
        self.parser = PythonParser()
        self.graph_builder = RepositoryGraph()

        self.db = None

        if uri and username and password:

            self.db = Neo4jManager(
                uri,
                username,
                password
            )

    def load_repository(self, repository_path):

        files = self.scanner.scan_python_files(
            repository_path
        )

        parsed_results = []

        for file in files:

            result = self.parser.parse_file(
                file
            )

            parsed_results.append(
                result
            )

        graph = self.graph_builder.build_repository_graph(
            parsed_results
        )

        if self.db:

            self.db.clear_database()

            for source, targets in graph.items():

                self.db.create_class_node(
                    source
                )

                for target in targets:

                    self.db.create_dependency(
                        source,
                        target
                    )

        return graph