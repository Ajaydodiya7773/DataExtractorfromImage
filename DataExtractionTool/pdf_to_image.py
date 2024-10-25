import fitz  # PyMuPDF

def pdf_to_images(pdf_path):
    doc = fitz.open(pdf_path)
    images = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()
        img_path = f"page_{page_num}.png"
        pix.save(img_path)
        images.append(img_path)
    return images
