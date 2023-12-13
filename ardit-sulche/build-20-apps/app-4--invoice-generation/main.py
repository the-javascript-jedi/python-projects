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
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    # excel name - 10001-2023.1.18.xlsx
    # using Path we can form an intelligent string, in this string .stem
    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    # invoice number
    pdf.set_font(family="Times", size=16, style="B")
    # ln=1 will break the line
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)

    # date
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date:{date}", ln=1)

    # df to get data for table
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # Add a header
    columns = df.columns
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=30, h=8, txt=str(columns[0]), border=1)
    pdf.cell(w=70, h=8, txt=str(columns[1]), border=1)
    pdf.cell(w=30, h=8, txt=str(columns[2]), border=1)
    pdf.cell(w=30, h=8, txt=str(columns[3]), border=1)
    pdf.cell(w=30, h=8, txt=str(columns[4]), border=1, ln=1)

    total_sum = 0
    # Add rows to the table
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)
        # total_sum=total_sum+float(row["total_price"])
        total_sum = df["total_price"].sum()
    pdf.cell(w=30, h=8, txt='', border=1)
    pdf.cell(w=70, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    # footer
    # add total sum sentence
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt=f"The total price is {total_sum}", ln=1)

    # add company name and logo
    pdf.set_font(family="Times", size=14)
    pdf.cell(w=30, h=8, txt="PythonHow")
    pdf.image("pythonhow.png", w=10)

    pdf.output(f"PDFs/{filename}.pdf")
