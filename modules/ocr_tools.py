# from pytesseract import image_to_string
# from pdf2image import convert_from_path
# import fitz  # PyMuPDF

# def extract_text_with_ocr(pdf_file):
#     pages = convert_from_path(pdf_file)
#     extracted_text = ""
#     for page in pages:
#         extracted_text += image_to_string(page)
#     return extracted_text


import tempfile
import pytesseract
from pdf2image import convert_from_path

def extract_text_with_ocr(uploaded_file):
    # Save the uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(uploaded_file.read())
        temp_pdf_path = temp_pdf.name  # Path to the temporary file

    # Convert the PDF to images
    pages = convert_from_path(temp_pdf_path, 300)  # Adjust DPI if needed

    # Extract text from each page using OCR
    extracted_text = ""
    for page in pages:
        text = pytesseract.image_to_string(page)
        extracted_text += text + "\n"

    # Optional: Clean up temporary file if needed
    # os.remove(temp_pdf_path)

    return extracted_text
