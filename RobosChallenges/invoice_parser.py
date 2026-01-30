import pdfplumber
import re


def extract_invoice_data(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages)

    def find(pattern):
        match = re.search(pattern, text)
        return match.group(1).strip() if match else ""

    return {
        "invoice_number": find(r"Invoice Number:\s*(.*)"),
        "invoice_date": find(r"Invoice Date:\s*(.*)"),
        "company_name": find(r"Company:\s*(.*)"),
        "total_due": find(r"Total Due:\s*\$?(.*)")
    }
