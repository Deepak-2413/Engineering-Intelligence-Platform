class ImpactAnalyzer:

    def find_impacted_components(self, graph, target):

        impacted = set()

        def dfs(node):

            for source, dependencies in graph.items():

                if node in dependencies and source not in impacted:

                    impacted.add(source)
                    dfs(source)

        dfs(target)

        return list(impacted)