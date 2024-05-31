import pdfkit
from PyPDF2 import PdfMerger

html_files = ["main_page.html", "second_page.html"]

pdf_files = ["f1.pdf", "f2.pdf"]

for html_file, pdf_file in zip(html_files, pdf_files):
    pdfkit.from_file(html_file, pdf_file)

merger = PdfMerger()

for pdf_file in pdf_files:
    merger.append(pdf_file)

output_pdf = "CV_skorychenko.pdf"
merger.write(output_pdf)
merger.close()
