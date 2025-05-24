from commonImports import *

'''
    Processes the Table B.1 scoring PDF by converting each page to a PNG 
    and cropping out individual scoring tables for further OCR processing.

    Parameters:
    - b1Pdf (str): File path to the Table B.1 PDF (pages 78–127 of the manual).
    - b1ImageFolder (str): Directory where full-page PNG images will be saved.
    - b1SplitImageFolder (str): Directory where cropped table images 
                                (Verbal1, Verbal2, Nonverbal) will be saved.

    This function wraps processPDF() with predefined file paths for Table B.1 
    and is the first step in the OCR pipeline for generating clean table inputs.
'''

def saveAllTable1Pages(b1Pdf, b1ImageFolder, b1SplitImageFolder):
    # Creates folders a
    os.makedirs(b1ImageFolder, exist_ok=True) 
    os.makedirs(b1SplitImageFolder, exist_ok=True)
    
    processPDF(b1Pdf, b1ImageFolder, b1SplitImageFolder)

# Copied from imageImport.py
def createAllFolders(startPage, endPage, outputFolder):
    for pageNum in range(startPage, endPage + 1):
        subfolderName = f'page_{pageNum}_all_CSV'
        subfolderPath = os.path.join(outputFolder, subfolderName)
        os.makedirs(subfolderPath, exist_ok=True)

def main():
    # File paths for Table B.1

    # File path to PDF containing all Table B.1 images
    b1Pdf = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\Research\KBIT-2 "
        r"Rapid Score\Book Pages\kbit_table_1_pages_78_127.pdf"
    )

    # File path to folder where PNGs of Table B.1 PDF pages will be saved
    b1ImageFolder = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\Research\KBIT-2 "
        r"Rapid Score\Table 1\Images"
    )

    # File path to folder where cropped Table B.1 images will be saved
    b1SplitImageFolder = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\Research\KBIT-2 "
        r"Rapid Score\Table 1\CSVs"
    )

    saveAllTable1Pages(b1Pdf, b1ImageFolder, b1SplitImageFolder)

main()