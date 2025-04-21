from commonImports import *
# Takes input from extractAllText
def cleanTextToList(text, table):
    cleanedData = []
    allLines = text.splitlines() # Turning each line into a list
    firstLine, lastLine = getNumericalValues(text, table) 
    selectedLines = allLines[firstLine: lastLine] # Only look at 
    # text that are part of the rows with numbers

    for line in selectedLines:
        line = cleanLine(line)
        if isValidLine(line):

def cleanLine(line):
    line = line.replace('|', ' ')
    line = line.replace('_', ' ')
    line = line.replace('—', '-')
    line = line.replace('=', ' ')
    # Tutorial: https://www.w3schools.com/python/python_regex.asp
    # Checks replaces any extra characters beyond the expected, the only 
    # characters remaining should be numbers (0-9), white space (\s), > and .
    # for decimal points
    line = re.sub(r'[^0-9\s>.]+', '', line)
    return line

def isValidLine(line):
    line = line.strip
    parts = line.split()
    if len(parts) is 4:
        rawScore = parts[0]
        standScore = parts[1]
        confInt = parts[2]
        percentile = parts[3]

        if rawScore

def getNumericalValues(text, table):
    startingVal = None
    startingRawScores = {'verbal1': 108, 
                        'verbal2': 51,
                        'nonverbal': 46}
                    
    for key in startingRawScores:
        if key is table:
            startingVal = startingRawScores[key]

    currLine = 0
    firstLine = None
    lastLine = None
    for line in text.splitlines():
        line = line.strip()
        
        if line.startswith(startingVal):
            firstLine = currLine
        
        if line.find('B.1') != -1 and currLine > firstLine:
            lastLine = currLine
            return  firstLine, lastLine
        
        currLine += 1

# def convertTextToCSV(data, outputFolder):
#     df = 
    
#     fileName = # Come back to this

def createVerbalDataFrame():
    rawScores = list(range(108, -1, -1)) # Because always these values
    df = pd.DataFrame({'Raw': rawScores})
    df.set_index('Raw', inplace = True) # Removes 0-index, makes raw score new index
    return df

def createNonverbalDataFrame():
    rawScores = list(range(46, -1, -1)) # Because always these values
    df = pd.DataFrame({'Raw': rawScores})
    df.set_index('Raw', inplace = True)
    return df