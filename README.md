# PDF Toolkit

This repository contains the code and resources for a **PDF Toolkit** application. The project provides various functionalities for **manipulating and enhancing PDFs**, making it a useful tool for document processing.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)

## Overview

The **PDF Toolkit** is a utility for performing operations such as **merging, splitting, rotating, annotating, extracting tables, converting to audio, and version control** for PDFs. It is built using **Python and Streamlit** for an interactive web-based experience.

## Features

- **Merge PDFs**: Combine multiple PDFs into one.
- **Split PDFs**: Extract specific pages from a PDF.
- **Rotate Pages**: Rotate individual or multiple pages in a PDF.
- **Annotate PDFs**: Highlight, underline, and add comments.
- **Extract Tables**: Convert tables from PDFs to CSV format.
- **Convert PDF to Audio**: Use **Text-to-Speech (TTS)** to generate audio from text.
- **Version Control**: Maintain document history and rollback to previous versions.

## Installation

To run this project locally, ensure you have Python installed. Then, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/SahilPitale06/PDF-Toolkit.git
   cd PDF-Toolkit
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   *Note: If `requirements.txt` is not available, manually install the necessary packages:*

   ```bash
   pip install streamlit PyMuPDF pdfplumber pytesseract gtts pandas
   ```

## Usage

1. **Run the Streamlit application:**

   ```bash
   streamlit run app.py
   ```

2. **Access the web interface:**

   Open a web browser and navigate to the **local Streamlit URL** displayed in the terminal. You can then interact with the various PDF tools available.

## Contributors

- [Sahil Pitale](https://github.com/SahilPitale06)

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

*Note: This README provides a general overview. For detailed explanations and code insights, refer to the Python scripts in the repository.*
