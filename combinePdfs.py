#! python3

# This code combines all the pdfs in the current working directory into a single file
# This is based on the similar exercise given in the book "Automate the boring stuff with Python"

import PyPDF2, os

# if PyPDF2 is not install, install using : pip install PyPDF2

# All the pdf filenames will be stored in the pdfFiles array
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort()

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the files
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Loop through all the pages
    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)              # Appending the page

# Save the resulting PDF to a file.
pdfOutput = open('combined_pdf.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
