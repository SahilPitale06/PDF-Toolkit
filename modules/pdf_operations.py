from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(files):
    writer = PdfWriter()
    for file in files:
        reader = PdfReader(file)
        for page in reader.pages:
            writer.add_page(page)
    output_file = "merged.pdf"
    with open(output_file, "wb") as f:
        writer.write(f)
    return output_file


def split_pdf(file, num_parts=None):
    """
    Splits a PDF into individual pages or into a specified number of parts.
    """
    reader = PdfReader(file)
    total_pages = len(reader.pages)
    
    split_files = []
    
    if num_parts and num_parts > 1:
        # Calculate how many pages per part
        pages_per_part = total_pages // num_parts
        for part in range(num_parts):
            writer = PdfWriter()
            start = part * pages_per_part
            end = start + pages_per_part if part < num_parts - 1 else total_pages
            for i in range(start, end):
                writer.add_page(reader.pages[i])
            output_file = f"split_part_{part + 1}.pdf"
            with open(output_file, "wb") as f:
                writer.write(f)
            split_files.append(output_file)
    else:
        # Split into individual pages
        for i, page in enumerate(reader.pages):
            writer = PdfWriter()
            writer.add_page(page)
            output_file = f"split_part_{i + 1}.pdf"
            with open(output_file, "wb") as f:
                writer.write(f)
            split_files.append(output_file)
    
    return split_files

def rearrange_pages(file, page_order, output_file="rearranged.pdf"):
    """
    Rearranges the pages of a PDF based on a given page order.
    """
    reader = PdfReader(file)
    writer = PdfWriter()
    for page_num in page_order:
        writer.add_page(reader.pages[page_num])
    with open(output_file, "wb") as f:
        writer.write(f)
    return output_file

def delete_pages(file, pages_to_delete, output_file="modified.pdf"):
    """
    Deletes specified pages from a PDF.
    """
    reader = PdfReader(file)
    writer = PdfWriter()
    for i, page in enumerate(reader.pages):
        if i not in pages_to_delete:
            writer.add_page(page)
    with open(output_file, "wb") as f:
        writer.write(f)
    return output_file

def update_metadata(file, metadata, output_file="updated_metadata.pdf"):
    """
    Updates the metadata of a PDF.
    """
    reader = PdfReader(file)
    writer = PdfWriter()
    
    # Copy all pages to the writer
    for page in reader.pages:
        writer.add_page(page)
    
    # Update metadata
    writer.add_metadata(metadata)
    
    with open(output_file, "wb") as f:
        writer.write(f)
    return output_file
