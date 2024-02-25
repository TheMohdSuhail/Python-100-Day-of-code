'''
Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge
multiple pdf files into a single pdf. You are welcome to add more functionalities

pypdf is a free and open-source pure-python PDF library capable of splitting, merging,
cropping, and transforming the pages of PDF files. It can also add custom data, viewing
options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.


'''

import pypdf

from pypdf import PdfMerger

import os



'''
for index in enumerate(dir(PdfWriter)):
    print(index)


'''



'''

files = os.listdir("Pdf")
i = 1
for file in files:

    if file.endswith(".pdf"):
        print(file)
        merger.append(file)

merger.write("merged-pdf.pdf")
merger.close()

'''





merger = PdfMerger()

files = os.listdir()

i = 1 

for file in files:

    if file.endswith(".pdf"):

        print(file)
       # os.rename(f"images\{file}", f"images\{i}.pdf")
        
        merger.append(file)
        i = i + 1
        
        
merger.write("result.pdf")
merger.close()


print(os.path.abspath(file))


























