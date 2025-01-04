# modules/pdf_utils.py
import os
import base64
import streamlit as st

def show_pdf(file_path):
    """Embed and display a PDF using PDF.js in Streamlit."""
    if os.path.exists(file_path):
        # Create a base64-encoded URL for the PDF
        with open(file_path, "rb") as pdf_file:
            pdf_data = base64.b64encode(pdf_file.read()).decode("utf-8")
            pdf_url = f"data:application/pdf;base64,{pdf_data}"

        # Embed PDF.js using an iframe and display the PDF
        st.components.v1.html(
            f"""
            <iframe src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.15.349/web/viewer.html?file={pdf_url}" width="700" height="500"></iframe>
            """,
            height=550,
        )
