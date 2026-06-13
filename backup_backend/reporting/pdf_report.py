from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


class PDFReportGenerator:

    def generate(
        self,
        report,
        output_file
    ):

        document = SimpleDocTemplate(
            output_file
        )

        styles = (
            getSampleStyleSheet()
        )

        content = []

        content.append(
            Paragraph(
                "Engineering Intelligence Report",
                styles["Title"]
            )
        )

        content.append(
            Spacer(1, 12)
        )

        for key, value in report.items():

            content.append(
                Paragraph(
                    f"<b>{key}</b>: {value}",
                    styles["BodyText"]
                )
            )

            content.append(
                Spacer(1, 6)
            )

        document.build(content)

        return output_file