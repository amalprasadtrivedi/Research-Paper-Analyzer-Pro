# pdf_parser.py
import fitz  # PyMuPDF
import streamlit as st
from typing import Union
from io import BytesIO


def extract_text(file: Union[str, BytesIO]) -> str:
    """
    Extracts and returns text from a PDF file.

    Args:
        file (str or BytesIO): Path to PDF file or uploaded file object.

    Returns:
        str: Full extracted text from the PDF.
    """
    try:
        # Open PDF file
        if isinstance(file, str):
            doc = fitz.open(file)
        else:
            doc = fitz.open(stream=file.read(), filetype="pdf")

        text = ""
        for page in doc:
            text += page.get_text()

        doc.close()
        return text.strip()

    except Exception as e:
        st.error(f"Failed to extract text from PDF: {e}")
        return ""


def extract_text_from_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        print(f"❌ Failed to extract text from {file_path}: {e}")
        return ""