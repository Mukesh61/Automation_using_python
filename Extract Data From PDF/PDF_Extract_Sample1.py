import PyPDF2

sample_file = open('sample.pdf','rb')

pdf_ref = PyPDF2.PdfFileReader(sample_file)

print(pdf_ref.numPages) #number of pages in PDF file

page_ref = pdf_ref.getPage(0)

text_of_pdf = page_ref.extractText()
print(text_of_pdf)

sample_file.close()
