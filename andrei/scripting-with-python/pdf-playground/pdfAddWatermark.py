import PyPDF2

# get the watermarked template to use, rb - read binary
template = PyPDF2.PdfFileReader(open('super.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
# add the watermark
output=PyPDF2.PdfFileWriter()

# for all pages apply the watermark
for i in range(template.getNumPages()):
    page=template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf','wb') as file:
        output.write(file)
