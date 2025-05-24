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
        subfolderName = f'page_{pageNum}'
        subfolderPath = os.path.join(outputFolder, subfolderName)
        os.makedirs(subfolderPath, exist_ok=True)

def testCSVPage(type):
    # Need a way to loop through this
    test = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project"
        r"\table_data_files\verbal2_page_80.png"
    )
    output = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project"
        r"\test_csv_files"
    )

    text = extractAllText(test)
    print(f'extractAll: {text}')
    cleanedList = cleanTextToList(text, type)

    df = listToDataFrame(cleanedList, type)
    dataFrameToCSV(df, type, output)

def saveTableCSVs(folderPath, tableType):
    b1ThresholdedImgFolder = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\Research"
        r"\KBIT-2 Rapid Score\test_1\thresholded_split_images"
    )
    os.makedirs(folderPath, exist_ok=True)
    startPage, endPage = 78, 127
    for pageNum in range(startPage, endPage + 1):
        fileName = f'{tableType}_page_{pageNum}.png'
        filePath = os.path.join(b1ThresholdedImgFolder, fileName)

        if os.path.exists(filePath):
            try:
                saveCSV(filePath, tableType, pageNum, folderPath)
            except Exception as exceptionStatement:
                print(f'Error on page {pageNum}: {exceptionStatement}')
        else:
            print(f'File not found: {filePath}')

# Input: File path to thresholded image, type of table, 
def saveCSV(filePath, tableType, pageNum, outputFolder):
    text = extractAllText(filePath)
    cleanedList = cleanTextToList(text, tableType)
    df = listToDataFrame(cleanedList, tableType)
    dataFrameToCSV(df, tableType, pageNum, outputFolder)

def main():
    b1PrelimCSVs = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\Research"
        r"\KBIT-2 Rapid Score\test_1\output_CSVs"
    )
    # createAllFolders(78, 127, b1PrelimCSVs)
    
    b1NonverbalCSVsFolder = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\Research"
        r"\KBIT-2 Rapid Score\test_1\all_nonverbal_CSVs"
    )

    # saveTableCSVs(b1NonverbalCSVsFolder, 'nonverbal')
    
    b1Verbal1CSVsFolder = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\Research"
        r"\KBIT-2 Rapid Score\test_1\all_verbal1_CSVs"
    )
    # saveTableCSVs(b1Verbal1CSVsFolder, 'verbal1')

    b1Verbal2CSVsFolder = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\Research"
        r"\KBIT-2 Rapid Score\test_1\all_verbal2_CSVs"
    )

    # saveTableCSVs(b1Verbal2CSVsFolder, 'verbal2')


main()