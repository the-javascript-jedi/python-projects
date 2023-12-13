from fpdf import FPDF
import glob
from pathlib import Path

# Create a list of text filepaths
filepaths = glob.glob("files/*.txt")
# Create one PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Go through each text file
for filepath in filepaths:
    # Add a page to the PDF document for each text file
    pdf.add_page()
    # Get the filename without the extension
    # and convert it to title case (e.g. Cat)
    filename = Path(filepath).stem
    name = filename.title()

    # Add the name to the PDF
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=name, ln=1)
    # Open the file in read mode ('r')
    with open(filepath, 'r') as file:
        # Read the contents of the file
        content = file.read()
        print(content)
        pdf.set_font(family="Times", size=16, style="B")
        # pdf.cell(w=50, h=8, txt=content, ln=1)
        # pdf.multi_cell(0, 10, content)
        pdf.multi_cell(w=0,h=15,txt=content)
# Produce the PDF
pdf.output("output.pdf")
