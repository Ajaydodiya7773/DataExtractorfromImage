import re

def extract_fields(text):
    fields = {}
    fields['party_name'] = re.search(r'Party Name:\s*(.*)', text).group(1) if re.search(r'Party Name:\s*(.*)', text) else ""
    fields['gstin'] = re.search(r'GSTIN:\s*([\d\w]+)', text).group(1) if re.search(r'GSTIN:\s*([\d\w]+)', text) else ""
    fields['item_name'] = re.search(r'Item Name:\s*(.*)', text).group(1) if re.search(r'Item Name:\s*(.*)', text) else ""
    fields['quantity'] = re.search(r'Quantity:\s*(\d+)', text).group(1) if re.search(r'Quantity:\s*(\d+)', text) else ""
    fields['total_amount'] = re.search(r'Total Amount:\s*([\d.]+)', text).group(1) if re.search(r'Total Amount:\s*([\d.]+)', text) else ""
    # Add more fields based on your requirements
    return fields
