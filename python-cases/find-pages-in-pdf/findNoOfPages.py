import PyPDF2

# Path to the uploaded PDF file
pdf_path = "./-Nithin_Samuel_Resume_July_2024_IJ-.pdf"

# Open the PDF file
with open(pdf_path, "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    num_pages = reader.numPages

num_pages