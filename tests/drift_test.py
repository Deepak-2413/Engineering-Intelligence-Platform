from backend.analysis.architecture_drift import (
    ArchitectureDriftAnalyzer
)

old_report = {

    "architecture_score": 80,
    "risk_score": 20,
    "technical_debt_hours": 40,
    "architecture_smells": [1, 2]
}

new_report = {

    "architecture_score": 65,
    "risk_score": 42,
    "technical_debt_hours": 70,
    "architecture_smells": [1, 2, 3, 4]
}

analyzer = (
    ArchitectureDriftAnalyzer()
)

result = analyzer.compare(
    old_report,
    new_report
)

print(result)