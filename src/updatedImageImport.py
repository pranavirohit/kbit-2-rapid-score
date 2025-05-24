from commonImports import *

def saveAllTable1Pages(b1Pdf, b1ImageFolder, b1CsvFolder):
    processPDF(b1Pdf, b1ImageFolder, b1CsvFolder)

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

    # File path to folder where cropped Table B.1 images will be saved
    b1ImageFolder = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\Research\KBIT-2 "
        r"Rapid Score\Table 1\Images"
    )

    # File path to folder where preliminary Table B.1 CSVs will be saved
    b1CsvFolder = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\Research\KBIT-2 "
        r"Rapid Score\Table 1\CSVs"
    )

    saveAllTable1Pages(b1Pdf, b1ImageFolder, b1CsvFolder)

main()