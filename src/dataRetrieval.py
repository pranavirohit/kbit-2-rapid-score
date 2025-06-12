'''
ADD ALL UPDATED FUNCTIONS TO COMMON IMPORTS ONCE DONE
'''
# Table B.1
# Will need to add a file directory searching mechanism to access the correct
# files, but first need to uploaded validated CSVs to GitHub
from commonImports import *

def findTableB1CSV(ageYears, ageMonths):
    # Logic to return filePath
    return 42

def readTableB1CSV(filePath, rawScore):
    df = pd.read_csv(filePath)
    row = df[df['Raw'] == rawScore]
    
    if not row.empty:
        rowAsDict = row.iloc[0].to_dict()
        standScore = rowAsDict['Standard']
        confInt = separateInterval(rowAsDict['ConfidenceInterval'])
        percentile = rowAsDict['Percentile']
        return standScore, confInt, percentile
    
    else:
        return 'Error', 'Error', 'Error'
    
def separateInterval(rangeVals):
    try:
        if '-' in rangeVals:
            bounds = [val.strip() for val in rangeVals.split('-')]
            return (int(bounds[0]), int(bounds[1]))
        elif '–' in rangeVals:
            return ValueError('Did not substitute - correctly')
        else:
            return ValueError('No dash found')
        
    except Exception as e:
        print(f'[!] separateInterval error: {e}')
        return(None, None)

def findTableB2CSV(ageYears, ageMonths):
    # Logic to return filePath
    return 42

def readTableB2CSV(standScoreSum):
    # Change to config.py setup later or relative file paths
    filePath = r"C:\Users\pkroh\OneDrive\Documents\GitHub\kbit-2-rapid-score\data\tables\iq_composite_page_1.csv"
    df = pd.read_csv(filePath)
    rowAsDict = findRowByScoreRange(df, standScoreSum, 'SumofStandardScores')
    
    # Changed parameters, since CSV file headings changed from Table B.1 to
    # Table B.2
    standScore = rowAsDict['StandScore']
    confInt = separateInterval(rowAsDict['90ConfInt'])
    percentile = rowAsDict['PercentileRank']
    return standScore, confInt, percentile

def findRowByScoreRange(df, score, rangeColumn):
    for i, row in df.iterrows():
        possibleRange = row[rangeColumn]
        if '-' in possibleRange:
            lowerBound, upperBound = separateInterval(possibleRange)
            if lowerBound <= score <= upperBound:
                return row.to_dict()
        else:
            if score == int(possibleRange):
                return row.to_dict()

# Table B.4
def processedTableB4CSV(standScore):
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
def testSeparateInterval():
    assert separateInterval('123 - 157') == (123, 157)
    assert separateInterval('123-157') == (123, 157)
    assert separateInterval('  45 -  78 ') == (45, 78)

    # Uses endash instead of hyphen
    assert separateInterval('80 – 120') == (None, None)
    assert separateInterval('123157') == (None, None)
    assert separateInterval('150 - ') == (None, None)
    assert separateInterval('- 160') == (None, None)
    assert separateInterval('abc - xyz') == (None, None)

# def testSignificanceLevel():
'''