# to run -  python pdfMerger.py dummy.pdf twopage.pdf tilt.pdf
# this python function will merge the pdfs into a single pdf
# to run the file  python pdf.py
import PyPDF2
#  to read pdf files we need to read it as a binary file
# rb will convert the file stream to a binary mode
import sys
# sys.argv[1:] - this will grab all arguments except the first (i.e) the script name
inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger=PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        # print the arguments after pdfMerger.py
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(inputs)
