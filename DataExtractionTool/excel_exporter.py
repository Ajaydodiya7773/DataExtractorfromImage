import pandas as pd

def save_to_excel(data, output_file="invoices.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
