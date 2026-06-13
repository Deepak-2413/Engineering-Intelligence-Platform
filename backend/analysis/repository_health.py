class RepositoryHealthAnalyzer:

    def analyze(self, graph):

        total_components = len(graph)

        total_dependencies = 0

        most_connected = None
        max_connections = -1

        for component, dependencies in graph.items():

            dependency_count = len(dependencies)

            total_dependencies += dependency_count

            if dependency_count > max_connections:

                max_connections = dependency_count
                most_connected = component

        if total_dependencies <= 3:
            health = "Good"
        elif total_dependencies <= 10:
            health = "Moderate"
        else:
            health = "Complex"

        return {
            "components": total_components,
            "dependencies": total_dependencies,
            "most_connected": most_connected,
            "health": health
        }