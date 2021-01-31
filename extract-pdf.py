#------------------------------------------------------------------------------
# Imports
import PyPDF2

#------------------------------------------------------------------------------
# Setup
pdfFileObj = open('Constitution.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#------------------------------------------------------------------------------
# Getting The Text
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

#------------------------------------------------------------------------------
# Close
pdfFileObj.close()

#------------------------------------------------------------------------------
