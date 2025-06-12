from commonImports import *
'''
ADD ALL UPDATED FUNCTIONS TO COMMON IMPORTS ONCE DONE
'''
# Table B.1
# Will need to add a file directory searching mechanism to access the correct
# files, but first need to uploaded validated CSVs to GitHub

def tableB1Values(outputDict):
    return 42

# Some seperation between retrieving verbal/nonverbal values?
def tableB1Nonverbal():
    return 42

def tableB1Verbal():
    return 42

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