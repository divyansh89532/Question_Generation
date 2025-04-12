# This file extract text from the pdf files 

# -------------------------
# PDF Extraction Utilities
# -------------------------

import fitz  # PyMuPDF
def extract_pages(pdf_path: str):
    """
    Extracts text from each page of the provided PDF file.
    :param pdf_path: Path to the PDF file.
    :return: List of strings, each corresponding to a page.
    """
    doc = fitz.open(pdf_path)
    pages = [page.get_text() for page in doc]
    return pages