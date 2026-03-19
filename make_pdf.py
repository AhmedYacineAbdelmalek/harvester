from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def create_cover_pdf(output_path):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    # Background
    c.setFillColorRGB(0.95, 0.95, 0.95)
    c.rect(0, 0, width, height, fill=1)

    # Fake logo
    c.setFillColorRGB(0.2, 0.3, 0.6)
    c.rect(50, height-150, 100, 100, fill=1)
    c.setFillColorRGB(1,1,1)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(70, height-110, "DHS")

    # Title
    c.setFillColorRGB(0,0,0)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(50, height-200, "CONFIDENTIAL")
    c.setFont("Helvetica", 18)
    c.drawString(50, height-240, "Internal Security Audit")

    # Fake content
    c.setFont("Helvetica", 12)
    text = """This document contains sensitive information regarding
the security posture of critical infrastructure.

Unauthorized disclosure is prohibited by federal law.

To view the full report, you must enable document content.
Please double-click the attachment icon below."""
    y = height - 300
    for line in text.split('\n'):
        c.drawString(50, y, line)
        y -= 20

    # Fake attachment icon
    c.setStrokeColorRGB(0,0,0)
    c.setFillColorRGB(0.8,0.8,0.8)
    c.rect(50, y-40, 40, 40, fill=1)
    c.setFillColorRGB(0,0,0)
    c.setFont("Helvetica", 8)
    c.drawString(55, y-25, "PDF")

    # Footer
    c.setFont("Helvetica-Oblique", 8)
    c.drawString(50, 30, "Classified • Do Not Distribute")
    c.save()

if __name__ == "__main__":
    create_cover_pdf("cover.pdf")