from fastapi.responses import FileResponse

from backend.reporting.pdf_report import (
    PDFReportGenerator
)


class ReportAPI:

    def generate_pdf(
        self,
        report
    ):

        generator = PDFReportGenerator()

        file_name = (
            "architecture_report.pdf"
        )

        generator.generate(
            report,
            file_name
        )

        return FileResponse(
            file_name,
            media_type="application/pdf",
            filename=file_name
        )