# Day 82
# Exercise 8: Merging the pdf.
from PyPDF2 import PdfWriter
import os

merge = PdfWriter()
files = [file for file in os.listdir() if file.endswith('.pdf')]

for pdf in files:
    merge.append(pdf)

merge.write("merge.pdf")
merge.close()