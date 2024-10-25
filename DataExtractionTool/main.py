from pdf_to_image import pdf_to_images
from ocr_extractor import extract_text_from_image
from field_extractor import extract_fields
from excel_exporter import save_to_excel

def process_invoice(file_path):
    images = pdf_to_images(file_path)
    all_data = []
    for image_path in images:
        text = extract_text_from_image(image_path)
        data = extract_fields(text)
        all_data.append(data)
    save_to_excel(all_data)

if __name__ == "__main__":
    file_path = "sample_invoice.pdf"  # Replace with your file path
    process_invoice(file_path)
    print("Data extraction complete. Check 'invoices.xlsx' for output.")
