from backend.reporting.pdf_report import (
    PDFReportGenerator
)

sample_report = {

    "components": 52,
    "dependencies": 439,
    "architecture_score": 37,
    "architecture_grade": "F",
    "technical_debt_level": "High"
}

generator = PDFReportGenerator()

file = generator.generate(
    sample_report,
    "architecture_report.pdf"
)

print(
    "PDF Generated:",
    file
)