class ArchitectureDriftAnalyzer:

    def compare(
        self,
        old_report,
        new_report
    ):

        score_change = (
            new_report["architecture_score"]
            - old_report["architecture_score"]
        )

        risk_change = (
            new_report["risk_score"]
            - old_report["risk_score"]
        )

        debt_change = (
            new_report["technical_debt_hours"]
            - old_report["technical_debt_hours"]
        )

        smell_change = (
            len(
                new_report["architecture_smells"]
            )
            -
            len(
                old_report["architecture_smells"]
            )
        )

        if score_change > 0:

            status = "Improved"

        elif score_change < 0:

            status = "Degraded"

        else:

            status = "Stable"

        return {

            "score_change":
                score_change,

            "risk_change":
                risk_change,

            "debt_change":
                debt_change,

            "smell_change":
                smell_change,

            "status":
                status
        }