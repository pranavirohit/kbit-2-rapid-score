'''
KBIT-2 Page Processor
This is where I plan to build out the complete data collection pipeline:
converting the scanned KBIT-2 scoring PDF into individual, labeled table images and
extracting raw text using OCR. 

Right now, this heavily uses the KBIT-2 Table Processing Helpers to:
- Convert the scanned PDF (Pages 78–84) into full-page PNGs
- Crop out individual Verbal and Nonverbal tables from each page
- Saves all PNGs to the folders on my desktop
- Runs OCR on one test nonverbal table image and prints the result (for debugging)

I plan to develop two algorithms, one to extract text from the Nonverbal table images,
and other to extract text from the Verbal table images. I want these functions
to put this data into a table/array format, and then use this to build
a dictionary for each table page (as each table page corresponds to a patient
age range.)

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

def testCSVPage():
    test = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\table_data_files\verbal1_page_78.png"
    output = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\csv_data_files"

    type = 'verbal1'
    text = extractAllText(test)
    cleanedList = cleanTextToList(text, type)
    df = listToDataFrame(cleanedList, type)
    dataFrameToCSV(df, type, output)

    

def main():
    testCSVPage()

main()