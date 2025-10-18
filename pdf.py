from fpdf import FPDF
import  pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin = 0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    #add header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln =1)
    for y in range(20,277,10):
       pdf.line(20, y, 200, y)
# ln - is for line break
#     pdf.line(10,21,200,22)

    #Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12,txt =row["Topic"], align='R')

    for i in range(row["Pages"]-1):
       pdf.add_page()
       pdf.ln(277)
       pdf.set_font(family = "Times", style="I", size= 8)
       pdf.set_text_color(100,180,180)
       pdf.cell(w=0, h=0, txt=row["Topic"],align ="R")
       for y in range(20, 277, 10):
           pdf.line(20, y, 200, y)

       pdf.ln(26)
pdf.output("output.pdf")