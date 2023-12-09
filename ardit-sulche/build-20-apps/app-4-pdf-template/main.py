from fpdf import FPDF

pdf = FPDF(orientation="P",unit="mm",format="A4")

# print(type(pdf))
pdf.add_page()

pdf.set_font(family="Times",style="B",size=12)
# w=0 - entire length of box
# ln=1 - break line add to next line
# h=12 - try to match font size with height
# align="L" - align left to right
pdf.cell(w=0,h=12,txt="Hello There!",align="L",ln=1,border=1)
# Ctrl + D copys the line
pdf.set_font(family="Times",style="B",size=9)
pdf.cell(w=0,h=12,txt="Hi There!",align="L",ln=1,border=1)
# output.pdf is generated in the file folder
pdf.output("output.pdf")