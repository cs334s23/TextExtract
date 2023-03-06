import io
import pdfminer.high_level
import pdfminer.layout
import pikepdf

# Open the PDF and attempt to repair it if necessary
pdf_path = "pikepdf_example/attachment_1.pdf"
try:
    pdf = pikepdf.open(pdf_path)
except pikepdf.PdfError as e:
    if isinstance(e.inner_exception, pikepdf.ReadError):
        pdf = pikepdf.open(pdf_path, recover=True)
    else:
        raise e

# Check if the PDF is already linearized
# Linearize the PDF
pdf.save(pdf_path, linearize=True)

# Extract all text from the PDF using pdfminer.six
with open(pdf_path, "rb") as f:
    pdf_bytes = io.BytesIO(f.read())
text = pdfminer.high_level.extract_text(pdf_bytes)

# Save the extracted text to a file
with open("pikepdf_example/attachment_1.txt", "w", encoding="utf-8") as f:
    f.write(text)
