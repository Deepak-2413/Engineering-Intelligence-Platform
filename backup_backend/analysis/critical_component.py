class CriticalComponentAnalyzer:

    def find_critical_components(self, graph):

        impact_count = {}

        for component in graph:
            impact_count[component] = 0

        for source, dependencies in graph.items():

            for dependency in dependencies:

                if dependency in impact_count:
                    impact_count[dependency] += 1

        sorted_components = sorted(
            impact_count.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return sorted_components