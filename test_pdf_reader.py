import fitz  # PyMuPDF

pdf_file = "hr_documents/payroll_policy.pdf"

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text() + "\n"
    except Exception as e:
        return f"Error reading PDF: {e}"
    return text

pdf_text = extract_text_from_pdf(pdf_file)
print("\n🔍 Extracted PDF Text:\n", pdf_text)
