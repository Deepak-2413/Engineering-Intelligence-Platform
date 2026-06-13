class AdvancedMetrics:

    def calculate(self, graph):

        components = len(graph)

        dependencies = sum(
            len(targets)
            for targets in graph.values()
        )

        if components == 0:
            return {
                "average_dependencies": 0,
                "dependency_density": 0,
                "coupling": "Low",
                "risk_score": 0
            }

        average_dependencies = (
            dependencies / components
        )

        max_possible = (
            components * (components - 1)
        )

        dependency_density = (
            dependencies / max_possible
            if max_possible > 0
            else 0
        )

        if dependency_density < 0.10:
            coupling = "Low"
        elif dependency_density < 0.30:
            coupling = "Medium"
        else:
            coupling = "High"

        risk_score = min(
            100,
            int(average_dependencies * 10)
        )

        return {
            "average_dependencies":
                round(average_dependencies, 2),

            "dependency_density":
                round(dependency_density, 3),

            "coupling":
                coupling,

            "risk_score":
                risk_score
        }