class ArchitectureScore:

    def calculate(
        self,
        risk_score,
        smell_count,
        security_count,
        cycle_found
    ):

        score = 100

        score -= risk_score // 2

        score -= smell_count * 2

        score -= security_count * 5

        if cycle_found:
            score -= 20

        score = max(0, score)

        if score >= 90:
            grade = "A"

        elif score >= 80:
            grade = "B"

        elif score >= 70:
            grade = "C"

        elif score >= 60:
            grade = "D"

        else:
            grade = "F"

        return {
            "architecture_score": score,
            "architecture_grade": grade
        }