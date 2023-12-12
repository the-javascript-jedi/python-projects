import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# take all files inside invoices with the extension .xlsx
# glob.glob will return an array of file names
filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    # loop 3 excels and create data frames for each
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()
    # excel name - 10001-2023.1.18.xlsx
    # using Path we can form an intelligent string, in this string .stem
    filename=Path(filepath).stem
    invoice_nr=filename.split("-")[0]
    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50,h=8,txt=f"Invoice nr.{invoice_nr}")
    pdf.output(f"PDFs/{filename}.pdf")