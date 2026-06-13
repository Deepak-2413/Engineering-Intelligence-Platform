
class GraphBuilder:

    def build_graph(self, parsed_data):

        graph = {}

        for class_name in parsed_data["classes"]:
            graph[class_name] = []

        for source, target in parsed_data["relationships"]:

            if source in graph:
                graph[source].append(target)

        return graph

    def print_graph(self, graph):

        print("\nDependency Graph Visualization:\n")

        for source, targets in graph.items():

            if not targets:
                print(source)

            for target in targets:
                print(f"{source} ---> {target}")