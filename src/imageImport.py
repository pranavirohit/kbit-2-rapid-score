'''
KBIT-2 Page Processor

This file is part of my KBIT-2 automation pipeline. It takes the scanned KBIT-2 scoring PDF 
(pages 78–84 from the test manual) and converts each page into a high-resolution PNG. 
From there, it uses helper functions to crop out the individual Verbal and Nonverbal tables, 
then runs OCR (Tesseract) on a test table image to extract the raw text. That text is cleaned 
and structured into a DataFrame, then saved as a CSV. 

Right now, this script already handles the full process for one test image: 
PDF conversion, table cropping, text extraction, data cleaning, and CSV output. 

Next, I plan to scale this to batch process all table images, saving cleaned CSVs for every page 
and renaming them so they reference the age range for the table, since that's what drives
most of the scoring values.

This file relies heavily on helper functions from imageProcessingFunctions.py for the image 
pipeline and dataExtractionFunctions.py for turning OCR output into usable structured data.

Here's what each function does:

- saveAllKBITPages():
    Uses processPDF to convert the PDF to page images and crops out table images.
    Then runs OCR on one test image (verbal1_page_78.png) and prints the result.

- testCSVPage(type):
    Tests the full pipeline from OCR to CSV on a single table image 
    (verbal2_page_80.png). Saves the output CSV to the test folder.

- saveCSV(filePath, tableType, pageNum, outputFolder):
    Full pipeline on a provided table image: runs OCR, cleans the text,
    formats the data into a DataFrame, and saves it to CSV.

- createAllFolders(startPage, endPage, outputFolder):
    Creates folders named page_XX_all_CSV to organize outputs by page.
    Useful for pre-organizing batch CSV outputs.

- main():
    Runs testCSVPage('verbal2') to test pipeline on one image.
    Commented-out code shows how to pre-generate output folders for pages 78–84.

'''

from commonImports import *

def saveAllKBITPages():
    # Please see the original PDF here: https://andrewcmu-my.sharepoint.com/:f:/g/personal/prohit_andrew_cmu_edu/EirgpWD3kpNOt-nRWhsru64B6oiYazECGSxTZTIrl-2cRw?e=Vj8j5y
    # Please see the resulting images, after my processing steps, 
    # here: https://andrewcmu-my.sharepoint.com/:f:/g/personal/prohit_andrew_cmu_edu/Ep0Xm_xR3JpFlH8T9YF1gBsBzG5KZ6V1T7sMO1jpHC3Xyw?e=DJo26d
    
    pdfKBIT = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\starter_files\KBIT_Pages_78_84.pdf"
    allKBITimages = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\data_files"
    allKBITtables = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\table_data_files"
    processPDF(pdfKBIT, allKBITimages, allKBITtables)

    testCroppedPage = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\table_data_files\verbal1_page_78.png"
    
    print(extractAllText(testCroppedPage))

def testCSVPage(type):
    test = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\table_data_files\verbal2_page_80.png"
    output = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\test_csv_files"

    text = extractAllText(test)
    print(f'extractAll: {text}')
    cleanedList = cleanTextToList(text, type)
    # print(cleanedList)

    df = listToDataFrame(cleanedList, type)
    dataFrameToCSV(df, type, output)

def saveCSV(filePath, tableType, pageNum, outputFolder):
    text = extractAllText(filePath)
    cleanedList = cleanTextToList(text, tableType)
    df = listToDataFrame(cleanedList, tableType)
    dataFrameToCSV(df, tableType, pageNum, outputFolder)

def createAllFolders(startPage, endPage, outputFolder):
    for pageNum in range(startPage, endPage + 1):
        subfolderName = f'page_{pageNum}_all_CSV'
        subfolderPath = os.path.join(outputFolder, subfolderName)
        os.makedirs(subfolderPath, exist_ok = True)

def main():
    testCSVPage('verbal2')
    # csvOutputFolder = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\csv_data_files"
    # createAllFolders(78, 84, csvOutputFolder)

main()