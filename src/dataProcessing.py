'''
Result Processing Placeholder

This file is meant to connect the user's selected output preferences 
(for example, which score categories they chose to include) with the actual 
KBIT-2 data loaded from the uploaded CSV or Excel file. 

Eventually, this function will take in the uploaded file, process the relevant 
score data, and generate a cleaned results DataFrame that reflects the user's 
selections.

Here's what each function does:

- processUploadedFile(app, filePath):
    Placeholder function for now. Will eventually read the uploaded CSV or Excel 
    file, filter it based on selected categories, and return the final results 
    table to be displayed or saved.

'''
from commonImports import *

# Add app parameter to connect to CSAcademy graphics in the future
# def processUploadedFile(app, filePath):

def processUploadedFile(filePath): 
    # Expecting an Excel file in example_data file format
    rowsAsDicts = createFileDict(filePath)
    print(rowsAsDicts)
    return 42

def createFileDict(filePath):
    df = pd.read_excel(filePath, engine="openpyxl", header=1)
    data = df.to_dict(orient="records")
    return data

# Table B.4
def descriptiveCategory(standScore):
    if standScore <= 69:
        return 'Lower extreme'
    elif 70 <= standScore <= 84:
        return 'Below average'
    elif 85 <= standScore <= 115:
        return 'Average'
    elif 116 <= standScore <= 130:
        return 'Above average'
    elif standScore >= 131:
        return 'Upper extreme'
    # Add exception here
    else:
        return 'Error'

# Table B.6
def significanceLevel(ageYears, verbalScore, nonverbalScore):
    difference = verbalScore - nonverbalScore
    significanceValues = {
        (4, 4): (17, 21),
        (5, 10): (15, 18),
        (11, 55): (13, 16),
        (56, 90): (12, 14)
    }
    for ageBounds in significanceValues:
        minAge = ageBounds[0]
        maxAge = ageBounds[1]
        if minAge <= ageYears <= maxAge:
            bounds = significanceValues[ageBounds]
            lowerBound = bounds[0]
            upperBound = bounds[1]
            
    if 0 <= difference < lowerBound:
        return 'Not Significant'
    elif lowerBound <= difference <= upperBound:
        return '<0.05'
    elif difference > upperBound:
        return '<0.01'
    else:
        return 'Error'

# Add test decorator, learn what test decorators do
'''
@test
def test(func):
    
def testSignificanceLevel():
'''

def main():
    testUploadedFile = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\Research\KBIT-2 Rapid Score\input_output_files\example_data.xlsx"
    processUploadedFile(testUploadedFile)

main()