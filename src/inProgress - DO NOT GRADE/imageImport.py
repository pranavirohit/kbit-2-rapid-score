'''
Used ChatGPT to reformat all lines to < 80 characters.
No changes to the actual code structure were made.
'''
from commonImports import *

def saveAllKBITPages():
    # Please see the original PDF here:
    # https://andrewcmu-my.sharepoint.com/:f:/g/personal/prohit_andrew_cmu_edu/
    # EirgpWD3kpNOt-nRWhsru64B6oiYazECGSxTZTIrl-2cRw?e=Vj8j5y

    # Please see the resulting images, after my processing steps, here:
    # https://andrewcmu-my.sharepoint.com/:f:/g/personal/prohit_andrew_cmu_edu/
    # Ep0Xm_xR3JpFlH8T9YF1gBsBzG5KZ6V1T7sMO1jpHC3Xyw?e=DJo26d

    pdfKBIT = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project"
        r"\starter_files\KBIT_Pages_78_84.pdf"
    )
    allKBITimages = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project"
        r"\data_files"
    )
    allKBITtables = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project"
        r"\table_data_files"
    )
    processPDF(pdfKBIT, allKBITimages, allKBITtables)

    testCroppedPage = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project"
        r"\table_data_files\verbal1_page_78.png"
    )

    print(extractAllText(testCroppedPage))

def testCSVPage(type):
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

def saveCSV(filePath, tableType, pageNum, outputFolder):
    text = extractAllText(filePath)
    cleanedList = cleanTextToList(text, tableType)
    df = listToDataFrame(cleanedList, tableType)
    dataFrameToCSV(df, tableType, pageNum, outputFolder)

def createAllFolders(startPage, endPage, outputFolder):
    for pageNum in range(startPage, endPage + 1):
        subfolderName = f'page_{pageNum}_all_CSV'
        subfolderPath = os.path.join(outputFolder, subfolderName)
        os.makedirs(subfolderPath, exist_ok=True)

def main():
    testCSVPage('verbal2')
    # csvOutputFolder = (
    #     r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\
    #     r"Term Project\csv_data_files"
    # )
    # createAllFolders(78, 84, csvOutputFolder)

main()
