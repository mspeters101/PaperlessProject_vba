import PyPDF2

document = open('myDocument.pdf',' rb') # Add path
pdf_reader = PyPDF2.PdfFileReader(document)
num_pages = pdf_reader.numPages
print('Reading Book')

for num in range(0, num_pages): #iterating through all pages
    page = pdf_reader.getPage(num)
    data = page.extractText()  #extracting text

   #include parsing logic
