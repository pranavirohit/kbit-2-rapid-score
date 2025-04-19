"""
This script is for one-time setup code.

Specifically, I'm using it to convert a scanned KBIT-2 PDF into separate
image files (one per page) using processPDF(). I only need to run this once 
to generate the image files, which I'll use in other parts of the project.

Not intended to be part of the core pipeline — just useful for preparing data.
"""
from commonImports import *

def saveAllKBITPages():
    pdfKBIT = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\starter_files\KBIT_Pages_78_84.pdf"
    allKBITimages = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\data_files"
    allKBITtables = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\table_data_files"
    processPDF(pdfKBIT, allKBITimages, allKBITtables)

def main():
    saveAllKBITPages()

main()

from commonImports import *

# verbalTest, nonVerbalTest = splitImage(testPage)

# Prints out a column of all the vertical lines!!
print(getVerticalLinesPositions(testPage))


# verbalProcessed = processImage(verbalTest)
# nonVerbalProcessed = processImage(nonVerbalTest)
# print(extractAllText(verbalProcessed))
# print(extractAllText(nonVerbalProcessed))