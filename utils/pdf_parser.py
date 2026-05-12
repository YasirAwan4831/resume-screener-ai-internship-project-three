import pdfplumber
from utils.logger import logger

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file using pdfplumber for better reliability.
    """
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text.strip()
    except Exception as e:
        logger.error(f"Error extracting text from PDF {pdf_path}: {str(e)}")
        return None
