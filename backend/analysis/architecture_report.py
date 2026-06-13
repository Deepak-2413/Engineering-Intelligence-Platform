from backend.analysis.repository_health import (
    RepositoryHealthAnalyzer
)

from backend.analysis.critical_component import (
    CriticalComponentAnalyzer
)

from backend.analysis.cycle_detector import (
    CycleDetector
)

from backend.analysis.advanced_metrics import (
    AdvancedMetrics
)

from backend.analysis.architecture_smells import (
    ArchitectureSmellDetector
)

from backend.analysis.architecture_score import (
    ArchitectureScore
)

from backend.analysis.technical_debt import (
    TechnicalDebtEstimator
)

from backend.analysis.refactoring_roadmap import (
    RefactoringRoadmap
)

from backend.security.security_scanner import (
    SecurityScanner
)

from backend.ai.refactoring_advisor import (
    RefactoringAdvisor
)


class ArchitectureReportGenerator:

    def generate(self, graph):

        health = RepositoryHealthAnalyzer()

        critical = CriticalComponentAnalyzer()

        cycles = CycleDetector()

        metrics = AdvancedMetrics()

        smell_detector = (
            ArchitectureSmellDetector()
        )

        security_scanner = (
            SecurityScanner()
        )

        score_calculator = (
            ArchitectureScore()
        )

        debt_estimator = (
            TechnicalDebtEstimator()
        )

        roadmap_generator = (
            RefactoringRoadmap()
        )

        advisor = (
            RefactoringAdvisor()
        )

        health_report = health.analyze(graph)

        critical_components = (
            critical.find_critical_components(graph)
        )

        has_cycle = cycles.detect_cycles(graph)

        advanced_metrics = (
            metrics.calculate(graph)
        )

        architecture_smells = (
            smell_detector.detect(graph)
        )

        security_findings = (
            security_scanner.scan(graph)
        )

        score_result = (
            score_calculator.calculate(
                advanced_metrics["risk_score"],
                len(architecture_smells),
                len(security_findings),
                has_cycle
            )
        )

        debt_result = (
            debt_estimator.estimate(
                len(architecture_smells),
                advanced_metrics["risk_score"],
                len(security_findings)
            )
        )

        refactoring_roadmap = (
            roadmap_generator.generate(
                architecture_smells,
                security_findings,
                advanced_metrics["risk_score"]
            )
        )

        recommendation_input = {

            "risk_score":
                advanced_metrics["risk_score"],

            "critical_components":
                critical_components,

            "architecture_smells":
                architecture_smells
        }

        refactoring_recommendations = (
            advisor.generate(
                recommendation_input
            )
        )

        report = {

            "components":
                health_report["components"],

            "dependencies":
                health_report["dependencies"],

            "health":
                health_report["health"],

            "most_connected":
                health_report["most_connected"],

            "average_dependencies":
                advanced_metrics[
                    "average_dependencies"
                ],

            "dependency_density":
                advanced_metrics[
                    "dependency_density"
                ],

            "coupling":
                advanced_metrics[
                    "coupling"
                ],

            "risk_score":
                advanced_metrics[
                    "risk_score"
                ],

            "architecture_score":
                score_result[
                    "architecture_score"
                ],

            "architecture_grade":
                score_result[
                    "architecture_grade"
                ],

            "technical_debt_hours":
                debt_result[
                    "technical_debt_hours"
                ],

            "technical_debt_level":
                debt_result[
                    "technical_debt_level"
                ],

            "architecture_smells":
                architecture_smells,

            "security_findings":
                security_findings,

            "security_risk_count":
                len(
                    security_findings
                ),

            "refactoring_roadmap":
                refactoring_roadmap,

            "refactoring_recommendations":
                refactoring_recommendations,

            "critical_components":
                critical_components[:10],

            "cycle_found":
                has_cycle,

            "all_nodes":
                list(graph.keys()),

            "dependency_graph":
                graph
        }

        return report