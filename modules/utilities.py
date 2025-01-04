import os
import streamlit as st

def upload_files(prompt, single=False):
    if single:
        file = st.file_uploader(prompt, type=["pdf"])
        if file:
            return file
    else:
        files = st.file_uploader(prompt, type=["pdf"], accept_multiple_files=True)
        if files:
            return files
    return None

def download_file(file_path, download_name):
    with open(file_path, "rb") as f:
        st.download_button(label=f"Download {download_name}", data=f, file_name=download_name)

def preview_file(file_path):
    st.text(f"Preview of {os.path.basename(file_path)}:")
    with open(file_path, "r") as f:
        st.text(f.read(500))
