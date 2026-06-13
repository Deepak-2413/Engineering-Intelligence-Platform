class ArchitectureSmellDetector:

    def detect(self, graph):

        smells = []

        for component, dependencies in graph.items():

            dependency_count = len(
                dependencies
            )

            if dependency_count > 20:

                smells.append({

                    "type":
                        "God Component",

                    "component":
                        component,

                    "details":
                        f"{component} has "
                        f"{dependency_count} dependencies"
                })

        return smells