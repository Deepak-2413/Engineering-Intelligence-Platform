
class PullRequestRiskAnalyzer:

    def analyze(
        self,
        changed_files,
        critical_components
    ):

        score = 0

        reasons = []

        critical_names = [
            component[0]
            for component in critical_components
        ]

        for file in changed_files:

            for component in critical_names:

                if component.lower() in file.lower():

                    score += 20

                    reasons.append(
                        f"Touches critical component: {component}"
                    )

        if score >= 80:

            level = "HIGH"

        elif score >= 40:

            level = "MEDIUM"

        else:

            level = "LOW"

        return {
            "risk_score": score,
            "risk_level": level,
            "reasons": reasons
        }
