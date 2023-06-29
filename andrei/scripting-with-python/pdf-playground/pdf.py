# to run the file  python pdf.py
import PyPDF2
#  to read pdf files we need to read it as a binary file
# rb will convert the file stream to a binary mode
with open('dummy.pdf','rb') as file:
    print("file",file)
    reader=PyPDF2.PdfFileReader(file)
    # read the no of files in pdf page
    print("reader.numPages", reader.numPages)
    # get particular pdf page number - eg get first page
    print("reader.getPage(1)", reader.getPage(0))
    # rotate the pdf page
    #  get the page to rotate
    page=reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer=PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf','wb') as new_file:
        writer.write(new_file)

