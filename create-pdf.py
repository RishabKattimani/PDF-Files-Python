#------------------------------------------------------------------------------
# Imports
from fpdf import FPDF

#------------------------------------------------------------------------------
# Setup
pdf = FPDF()

# Add a page
pdf.add_page()

# Set Style & Font
pdf.set_font("Arial", size = 15)

# Create a Cell
pdf.cell(200, 10, txt = "Rishab's Report",
		ln = 1, align = 'C')

# Next Line
pdf.cell(200, 10, txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
		ln = 2, align = 'C')
#------------------------------------------------------------------------------
# Saving the PDF

pdf.output("sdfghjI .pdf")
