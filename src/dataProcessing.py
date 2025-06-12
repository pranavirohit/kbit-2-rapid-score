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
    for row in rowsAsDicts:
        participant = buildParticipantResults(row)
        print(participant)
    return 42

def createFileDict(filePath):
    df = pd.read_excel(filePath, engine="openpyxl", header=1)
    data = df.to_dict(orient="records")
    return data

def buildParticipantResults(row):
    # Expecting a dictionary with the parameters of the input file, reads in
    # five values directly
    id = row['Participant ID']

    # In the future, retrieve age information through algorithm that calculates
    # both from test date and birth date of participant
    ageYears = row['Age (Years)']
    ageMonths = row['Age (Months)']

    verbalKnowledgeRaw = row['Verbal Knowledge']
    riddlesRaw = row['Riddles']
    matricesRaw = row['Matrices']

    participant = {
        'Participant ID': id,
        'Age (Years)': ageYears,
        'Age (Months)': ageMonths,

        # Raw Scores
        'Verbal Knowledge': verbalKnowledgeRaw, # A1
        'Riddles': riddlesRaw, # A2
        'Matrices': matricesRaw, # A3

        # Total Raw Scores
        'Raw Verbal Total': verbalKnowledgeRaw + riddlesRaw, # B1 = A1 + A2
        'Raw Nonverbal Total': matricesRaw, # B2 = A3

        # Table B.1 Values (Verbal)
        # 90% CI represents 90% Confidence Interval, PR represents Percentile
        # Rank
        'Standard Verbal': None, # C1
        '90% CI Verbal': (None, None), # D1A, D1B
        'PR Verbal': None, # E1C

        # Table B.1 Values (Nonverbal)
        'Standard Nonverbal': None, # C2
        '90% CI Nonverbal': (None, None), # D2A, D2B
        'PR Nonverbal': None, # E2C

        'Standard Sum': None, # C3 = C1 + C2
        
        # Table B.2 Values
        'Standard IQ': None, # C4
        '90% CI IQ': (None, None), # D3A, D3B
        'PR IQ': None, # E3C

        # Table B.3 Values
        'PR Verbal Range': (None, None), # E1A, E1B
        'PR Nonverbal Range': (None, None), # E2A, E2B
        'PR IQ Range': (None, None), # E3A, E3B

        # Table B.4 Values
        'Descriptive Verbal': None, # F1
        'Descriptive Nonverbal': None, # F2
        'Descriptive IQ': None, # F3

        # Table B.5 Values
        'Age Equivalent Verbal': None, # G1
        'Age Equivalent Nonverbal': None, # G2
        
        # Table B.6 Values
        'Score Difference': None, # H1
        'Significance Level': None, # H2
        'Frequency of Occurence': None, # H3

    }

    writeTableB1Values(participant)
    writeTableB2Values(participant)
    writeTableB4Values(participant)
    writeTableB6Values(participant)

    return participant

def writeTableB1Values(outputDict):
    # Manually adding file paths for now, will replace with search algorithm
    # in the future
    b1VerbalCSV = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\Research\KBIT-2 Rapid Score\test_1\fixed_all_verbal2_CSVs\verbal2_page_78_fixed.csv"
    b1NonverbalCSV = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\Research\KBIT-2 Rapid Score\test_1\fixed_all_nonverbal_CSVs\nonverbal_page_78_fixed.csv"

    verbalRawTotal = outputDict['Raw Verbal Total']
    verbalScores = readTableB1CSV(b1VerbalCSV, verbalRawTotal)

    # Standard Verbal, 90% CI Verbal, PR Verbal
    outputDict['Standard Verbal'] = verbalScores[0]
    outputDict['90% CI Verbal'] = verbalScores[1]
    outputDict['PR Verbal'] = verbalScores[2]

    nonverbalRawTotal = outputDict['Raw Nonverbal Total']
    nonverbalScores = readTableB1CSV(b1NonverbalCSV, nonverbalRawTotal)

    # Standard Nonverbal, 90% CI Nonverbal, PR Nonverbal
    outputDict['Standard Nonverbal'] = nonverbalScores[0]
    outputDict['90% CI Nonverbal'] = nonverbalScores[1]
    outputDict['PR Nonverbal'] = nonverbalScores[2]

    # Standard Sum
    outputDict['Standard Sum'] = verbalScores[0] + nonverbalScores[0]

def writeTableB2Values(outputDict):
    standScoreSum = outputDict['Standard Sum']
    iqScores = readTableB2CSV(standScoreSum)

    # Standard IQ, 90% CI IQ, PR IQ
    outputDict['Standard IQ'] = iqScores[0]
    outputDict['90% CI IQ'] = iqScores[1]
    outputDict['PR IQ'] = iqScores[2]

def writeTableB4Values(outputDict):
    standVerbal = outputDict['Standard Verbal']
    standNonverbal = outputDict['Standard Nonverbal']

    outputDict['Descriptive Verbal'] = processedTableB4CSV(standVerbal)
    outputDict['Descriptive Nonverbal'] =  processedTableB4CSV(standNonverbal)

def writeTableB6Values(outputDict):
    ageYears = outputDict['Age (Years)']
    standVerbal = outputDict['Standard Verbal']
    standNonverbal = outputDict['Standard Nonverbal']
    
    # Score Difference (adjusted to be absolute value of standard scores)
    outputDict['Score Difference'] = abs(standVerbal - standNonverbal)
    
    difference = outputDict['Score Difference']
    # Significance Level
    outputDict['Significance Level'] = processedTableB6CSV(ageYears, difference)

def main():
    testUploadedFile = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\Research\KBIT-2 Rapid Score\input_output_files\example_data.xlsx"
    processUploadedFile(testUploadedFile)

main()

'''
    Formatting for output file, check back on this because there will be
    repeat values

    participant = {
        'Participant ID': id,
        'Age (Years)': ageYears,
        'Age (Months)': ageMonths,

        # Scoring Information
        'Verbal Knowledge': verbalKnowledgeRaw,
        'Riddles': riddlesRaw,
        'Matrices': matricesRaw,

        # Verbal Results
        'Total Raw Scores': verbalKnowledgeRaw + riddlesRaw,
        'Standard Score': None,
        '90% Confidence Interval': None,
        'Percentile Rank': None,
        'Descriptive Category': None,
        'Age Equivalent': None,

        # Nonverbal Results




    }
'''