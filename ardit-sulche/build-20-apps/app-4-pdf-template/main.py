from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P",unit="mm",format="A4")

df=pd.read_csv("topics.csv")

for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(0,0,0)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    #line coordinates -- pdf.line(x1,y1,x2,y2)
    pdf.line(10,21,200,21)

# output.pdf is generated in the file folder
pdf.output("output.pdf")