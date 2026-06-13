class RefactoringRoadmap:

    def generate(
        self,
        smells,
        security_findings,
        risk_score
    ):

        roadmap = []

        if security_findings:

            roadmap.append({
                "priority": 1,
                "action":
                    "Resolve security issues"
            })

        if len(smells) > 0:

            roadmap.append({
                "priority": 2,
                "action":
                    "Refactor God Components"
            })

        if risk_score > 70:

            roadmap.append({
                "priority": 3,
                "action":
                    "Reduce component coupling"
            })

        roadmap.append({
            "priority": 4,
            "action":
                "Improve modularization"
        })

        roadmap.append({
            "priority": 5,
            "action":
                "Increase test coverage"
        })

        return roadmap