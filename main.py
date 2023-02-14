import fpdf
import pandas as pd

df = pd.read_csv('topics.csv')
pdf = fpdf.FPDF(orientation='P', unit='mm', format='A4')

for index, row in df.iterrows():
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=12)
    pdf.set_text_color(r=100, g=100, b=100)
    pdf.cell(w=0, h=12, txt=row["Topic"], border=0, ln=1, align='L')
    pdf.line(10, 20, 200, 20)

    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(r=100, g=100, b=100)
    pdf.cell(w=0, h=12, txt=row["Topic"], border=0, ln=1, align='R')

    for i in range(row['Pages']-1):
        pdf.add_page()

        pdf.ln(277)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(r=100, g=100, b=100)
        pdf.cell(w=0, h=12, txt=row["Topic"], border=0, ln=1, align='R')

pdf.output('test.pdf')
