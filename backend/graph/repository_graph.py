class RepositoryGraph:

    def build_repository_graph(self, parsed_results):

        graph = {}

        for result in parsed_results:

            for class_name in result["classes"]:

                if class_name not in graph:
                    graph[class_name] = []

            for source, target in result["relationships"]:

                if source not in graph:
                    graph[source] = []

                graph[source].append(target)

        return graph