from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
# remove automatic page break
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    # draw blank lines  #line coordinates -- pdf.line(x1,y1,x2,y2)
    # start at 20 till 298 with 10 distance between each line
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)
    # add footer for all pages
    # set position of footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

    # each topic has a set of pages - use nested for loop
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # add footer for all pages
        # set position of footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")
        for i in range(10):
            pdf.set_draw_color(0, 0, 0)
            pdf.cell(w=0, h=12, txt="Hello", align="R", ln=1, border=1)
            pdf.line(10, 21, 200, 21)
            for y in range(20, 298, 10):
                pdf.line(10, y, 200, y)

# output.pdf is generated in the file folder
pdf.output("output.pdf")
