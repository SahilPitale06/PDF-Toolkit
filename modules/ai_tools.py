# from transformers import pipeline

# def summarize_pdf(pdf_file):
#     summarizer = pipeline("summarization")
#     with open(pdf_file, "rb") as f:
#         text = f.read().decode('utf-8', errors="ignore")
#     summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
#     return summary[0]['summary_text']

# def extract_keywords(pdf_file):
#     # Placeholder for keyword extraction logic
#     keywords = ["example", "PDF", "toolkit"]
#     return keywords


# from transformers import pipeline
# from PyPDF2 import PdfReader

# def summarize_pdf(uploaded_file):
#     """
#     Summarize a PDF file from an UploadedFile object.
#     """
#     summarizer = pipeline("summarization")
    
#     # Read the content from the UploadedFile object
#     pdf_reader = PdfReader(uploaded_file)
#     text = ""
#     for page in pdf_reader.pages:
#         text += page.extract_text()
    
#     # Perform summarization
#     # Truncate or chunk text as required to meet the model input size
#     max_input_length = 1024  # Adjust based on model capacity
#     truncated_text = text[:max_input_length]
    
#     summary = summarizer(truncated_text, max_length=130, min_length=30, do_sample=False)
#     return summary[0]['summary_text']


from transformers import pipeline
from PyPDF2 import PdfReader

def summarize_pdf(uploaded_file):
    """
    Summarize a PDF file from an UploadedFile object.
    """
    summarizer = pipeline("summarization")
    
    # Read the content from the UploadedFile object
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    # Define model limits and chunking
    max_input_length = 1024  # Maximum tokens the model can process
    max_summary_length = 650  # Summary length per chunk
    min_summary_length = 100  # Minimum to ensure coherence
    
    # Break the document into manageable chunks
    chunks = [text[i:i + max_input_length] for i in range(0, len(text), max_input_length)]
    
    # Summarize each chunk and combine summaries
    summaries = []
    for chunk in chunks:
        summary = summarizer(
            chunk,
            max_length=max_summary_length,
            min_length=min_summary_length,
            do_sample=False,
        )
        summaries.append(summary[0]['summary_text'])
    
    # Combine individual summaries into a single summary
    combined_summary = " ".join(summaries)
    
    # Ensure the combined summary is no longer than 2000 words
    combined_words = combined_summary.split()
    final_summary = " ".join(combined_words[:2000])  # Limit to 2000 words
    
    return final_summary

def extract_keywords(uploaded_file):
    """
    Placeholder for keyword extraction logic.
    """
    keywords = ["example", "PDF", "toolkit"]
    return keywords
