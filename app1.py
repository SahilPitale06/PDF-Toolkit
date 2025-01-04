import streamlit as st
import os
import tempfile
from modules.pdf_operations import merge_pdfs, split_pdf, rearrange_pages, delete_pages
from modules.conversion_tools import (
    convert_to_word,
    convert_to_image,
    convert_to_excel,
    convert_to_epub
)
from modules.ocr_tools import extract_text_with_ocr
from modules.ai_tools import summarize_pdf, extract_keywords
from modules.utilities import upload_files, download_file
from modules.localization import translate_app

# App Configuration
st.set_page_config(page_title="PDF Toolkit", layout="wide")

# Localization
selected_language = st.sidebar.selectbox("Choose Language", ["English", "Español", "Français"])
translations = translate_app(selected_language)

# Sidebar - Feature Selection
feature = st.sidebar.radio(
    "Choose a Feature",
    [
        "Home",
        "Merge PDFs",
        "Split PDF",
        "Rearrange Pages",
        "Delete Pages",
        "Convert to Other Formats",
        "OCR Text Extraction",
        "Summarize and Analyze",
        "Settings",
    ],
)

# Check if a file is already uploaded in session state
if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []

# Home Screen - File Upload
if feature == "Home":
    st.title("Welcome to the PDF Toolkit")
    st.write("Upload your PDF files here to access all the available features.")
    uploaded_files = upload_files("Upload PDF files", single=False)  # Allow multiple files

    if uploaded_files:
        st.session_state.uploaded_files = uploaded_files
        st.success("Files uploaded successfully!")
    elif uploaded_files is not None:
        st.warning("Please upload PDF files to proceed.")
    
    # Display uploaded files list
    if st.session_state.uploaded_files:
        st.write("Uploaded Files:")
        for i, file in enumerate(st.session_state.uploaded_files):
            st.write(f"{i + 1}: {file.name}")
    
elif feature == "Merge PDFs":
    if st.session_state.uploaded_files:
        st.title("Merge PDFs")
        if len(st.session_state.uploaded_files) > 1:
            if st.button("Merge PDFs"):
                try:
                    merged_pdf = merge_pdfs(st.session_state.uploaded_files)
                    download_file(merged_pdf, "Merged_PDF.pdf")
                    st.success("PDFs merged successfully!")
                except Exception as e:
                    st.error(f"Error merging PDFs: {e}")
        else:
            st.warning("Please upload at least two PDF files to merge.")
    else:
        st.warning("Please go to the Home screen and upload PDF files first.")

elif feature == "Split PDF":
    if st.session_state.uploaded_files:
        st.title("Split PDF")
        split_type = st.radio("Split Options", ["By Number of Pages", "Into Parts"])

        if split_type == "By Number of Pages":
            num_pages = st.number_input("Enter the number of pages per part:", min_value=1, step=1)
        elif split_type == "Into Parts":
            num_parts = st.number_input("Enter the number of parts:", min_value=1, step=1)

        if st.button("Split"):
            try:
                if split_type == "By Number of Pages":
                    split_pdfs = split_pdf(st.session_state.uploaded_files[0], num_pages=num_pages)
                elif split_type == "Into Parts":
                    split_pdfs = split_pdf(st.session_state.uploaded_files[0], num_parts=num_parts)

                for i, pdf in enumerate(split_pdfs):
                    download_file(pdf, f"Split_Part_{i + 1}.pdf")
                st.success("PDF split successfully!")
            except Exception as e:
                st.error(f"Error splitting PDF: {e}")
    else:
        st.warning("Please go to the Home screen and upload PDF files first.")

elif feature == "Rearrange Pages":
    if st.session_state.uploaded_files:
        st.title("Rearrange Pages")
        page_order = st.text_input("Enter page order (comma-separated):", "0,1,2")
        if st.button("Rearrange"):
            try:
                page_order = list(map(int, page_order.split(',')))
                rearranged_pdf = rearrange_pages(st.session_state.uploaded_files[0], page_order)
                download_file(rearranged_pdf, "Rearranged_PDF.pdf")
            except ValueError:
                st.error("Invalid page order format!")
    else:
        st.warning("Please go to the Home screen and upload PDF files first.")

elif feature == "Delete Pages":
    if st.session_state.uploaded_files:
        st.title("Delete Pages")
        pages_to_delete = st.text_input("Enter pages to delete (comma-separated):", "0")
        if st.button("Delete"):
            try:
                pages_to_delete = list(map(int, pages_to_delete.split(',')))
                modified_pdf = delete_pages(st.session_state.uploaded_files[0], pages_to_delete)
                download_file(modified_pdf, "Modified_PDF.pdf")
            except ValueError:
                st.error("Invalid page numbers!")
    else:
        st.warning("Please go to the Home screen and upload PDF files first.")

elif feature == "Convert to Other Formats":
    if st.session_state.uploaded_files:
        st.title("Convert to Other Formats")
        output_format = st.selectbox("Select Format", ["Word", "Excel", "Image", "ePub"])

        if st.button("Convert"):
            uploaded_file = st.session_state.uploaded_files[0]
            
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.getbuffer())
                temp_pdf_path = tmp_file.name

            try:
                conversion_functions = {
                    "Word": convert_to_word,
                    "Excel": convert_to_excel,
                    "Image": lambda x: convert_to_image(x)[0],
                    "ePub": convert_to_epub
                }
                
                if output_format in conversion_functions:
                    converted_file = conversion_functions[output_format](temp_pdf_path)
                    
                    output_extension = output_format.lower()
                    if output_format == "Word":
                        output_extension = "docx"
                        
                    output_filename = f"Converted_File.{output_extension}"
                    
                    download_file(converted_file, output_filename)
                    st.success(f"PDF converted to {output_format} successfully!")
                else:
                    st.error(f"Unsupported output format: {output_format}")
                    
            except FileNotFoundError:
                st.error("The source PDF file was not found")
            except PermissionError:
                st.error("Permission denied while accessing the file")
            except Exception as e:
                st.error(f"Error converting PDF: {str(e)}")
            finally:
                if os.path.exists(temp_pdf_path):
                    try:
                        os.remove(temp_pdf_path)
                    except:
                        pass
                if converted_file and os.path.exists(converted_file):
                    try:
                        os.remove(converted_file)
                    except:
                        pass
    else:
        st.warning("Please go to the Home screen and upload PDF files first.")

elif feature == "OCR Text Extraction":
    if st.session_state.uploaded_files:
        st.title("OCR Text Extraction")
        extracted_text = extract_text_with_ocr(st.session_state.uploaded_files[0])
        st.text_area("Extracted Text", value=extracted_text, height=200)
    else:
        st.warning("Please go to the Home screen and upload PDF files first.")

elif feature == "Summarize and Analyze":
    if st.session_state.uploaded_files:
        st.title("Summarize and Analyze")
        if st.button("Summarize"):
            try:
                summary = summarize_pdf(st.session_state.uploaded_files[0])
                st.write("Summary:", summary)
            except Exception as e:
                st.error(f"Error summarizing PDF: {e}")
        if st.button("Extract Keywords"):
            try:
                keywords = extract_keywords(st.session_state.uploaded_files[0])
                st.write("Keywords:", ", ".join(keywords))
            except Exception as e:
                st.error(f"Error extracting keywords: {e}")
    else:
        st.warning("Please go to the Home screen and upload PDF files first.")


elif feature == "Settings":
    st.title("Settings")
    st.write("Configure app preferences here.")
    # Add settings-related options like theme customization, language selection, etc.

# Footer
st.sidebar.info("Developed by [Sahil Pitale]")
