class RefactoringAdvisor:

    def generate(self, report):

        recommendations = []

        risk_score = report.get(
            "risk_score",
            0
        )

        critical = report.get(
            "critical_components",
            []
        )

        smells = report.get(
            "architecture_smells",
            []
        )

        if risk_score > 70:

            recommendations.append(
                {
                    "priority": "High",
                    "action":
                        "Reduce coupling between modules",
                    "benefit":
                        "Lower architecture risk"
                }
            )

        for smell in smells:

            if (
                isinstance(smell, dict)
                and smell.get("type")
                == "God Component"
            ):

                recommendations.append(
                    {
                        "priority": "High",
                        "action":
                            f"Split {smell['component']} into smaller modules",
                        "benefit":
                            "Improve maintainability"
                    }
                )

        for component in critical[:5]:

            recommendations.append(
                {
                    "priority": "Medium",
                    "action":
                        f"Review dependencies of {component[0]}",
                    "benefit":
                        "Reduce architectural complexity"
                }
            )

        return recommendations