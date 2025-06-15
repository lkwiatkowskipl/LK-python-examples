import fitz  # PyMuPDF
from pathlib import Path
import re
import textwrap
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

# 📁 Folder PDF-ów
pdf_folder = Path(r"C:\B")
output_pdf_path = pdf_folder / "scalony_output_notebookLM_wrapped.pdf"

# ✅ Dozwolone znaki
ALLOWED_CHARS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,;:!?()[]{}<>\"'-\n\t")

def clean_text(text):
    text = re.sub(r'[\u200B-\u200D\uFEFF\u00A0]', ' ', text)
    cleaned = ''.join(c if c in ALLOWED_CHARS else ' ' for c in text)
    cleaned = re.sub(r'[ \t]{2,}', ' ', cleaned)
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
    lines = cleaned.split('\n')
    wrapped = []
    for line in lines:
        wrapped.extend(textwrap.wrap(line, width=100))  # zawijanie każdej linii
    return wrapped

# 🔧 Parametry strony
c = canvas.Canvas(str(output_pdf_path), pagesize=A4)
width, height = A4
x_margin = 20 * mm
y_margin = 20 * mm
line_height = 12
max_lines_per_page = int((height - 2 * y_margin) / line_height)
y_position = height - y_margin
line_count = 0

for pdf_file in sorted(pdf_folder.glob("*.pdf")):
    try:
        doc = fitz.open(pdf_file)
        full_text = ""
        for page in doc:
            raw = page.get_text("text")
            if raw.strip():
                full_text += raw

        cleaned_lines = clean_text(full_text)
        if cleaned_lines:
            c.setFont("Helvetica-Bold", 12)
            c.drawString(x_margin, y_position, f"### {pdf_file.name}")
            y_position -= line_height
            line_count += 1

            c.setFont("Helvetica", 10)
            for line in cleaned_lines:
                if line_count >= max_lines_per_page or y_position <= y_margin:
                    c.showPage()
                    y_position = height - y_margin
                    line_count = 0
                    c.setFont("Helvetica", 10)
                c.drawString(x_margin, y_position, line)
                y_position -= line_height
                line_count += 1

    except Exception as e:
        print(f"Błąd przetwarzania pliku {pdf_file.name}: {e}")

c.save()
print(f"\n✅ Gotowe: {output_pdf_path}")
