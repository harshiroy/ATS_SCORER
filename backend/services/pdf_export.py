from reportlab.pdfgen import canvas
from io import BytesIO
import logging
import traceback

logger = logging.getLogger("ats_resume_scorer")

def generate_combined_pdf(html_docs: dict[str, str]) -> bytes:
    try:
        buffer = BytesIO()
        c = canvas.Canvas(buffer)

        y = 800
        c.setFont("Helvetica", 10)

        for name, html_str in html_docs.items():
            c.drawString(50, y, f"=== {name.upper()} ===")
            y -= 20

            for line in str(html_str).split("\n"):
                if y < 50:
                    c.showPage()
                    c.setFont("Helvetica", 10)
                    y = 800

                c.drawString(50, y, line[:120])
                y -= 15

            y -= 25

        c.save()
        buffer.seek(0)

        return buffer.getvalue()

    except Exception as e:
        traceback.print_exc()
        logger.exception("PDF generation failed")
        raise