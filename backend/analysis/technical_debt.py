class TechnicalDebtEstimator:

    def estimate(
        self,
        smell_count,
        risk_score,
        security_count
    ):

        debt_hours = (
            smell_count * 4
            + security_count * 8
            + risk_score // 5
        )

        if debt_hours < 20:
            level = "Low"

        elif debt_hours < 50:
            level = "Medium"

        elif debt_hours < 100:
            level = "High"

        else:
            level = "Critical"

        return {
            "technical_debt_hours":
                debt_hours,

            "technical_debt_level":
                level
        }