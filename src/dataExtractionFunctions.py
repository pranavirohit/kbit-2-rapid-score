from commonImports import *

def extractAllText(filePath):
    image = PILImage.open(filePath)
    text = pyt.image_to_string(image, config = '--psm 6')
    return text

# Takes input from extractAllText
def cleanTextToList(text, tableType):
    cleanedData = []
    allLines = text.splitlines() # Turning each line into a list
    firstLine, lastLine = getNumericalValues(text, tableType) 
    selectedLines = allLines[firstLine: lastLine] # Only look at 
    # text that are part of the rows with numbers

    for line in selectedLines:
        line = cleanLine(line)
        
        if isValidLength(line):
            line = line.strip
            parts = line.split()

            rawScore = int(parts[0])
            standScore = int(parts[1])
            confInt = parts[2]
            percentile = parts[3]

            cleanedData.append({
                'Raw': rawScore,
                'Standard': standScore,
                'ConfidenceInterval': confInt,
                'Percentile': percentile
            })

    return cleanedData

def cleanLine(line):
    line = line.replace('|', ' ')
    line = line.replace('_', ' ')
    line = line.replace('—', '-')
    line = line.replace('=', ' ')
    line = checkDecimalPoints(line)

    # Tutorial: https://www.w3schools.com/python/python_regex.asp
    # Checks replaces any extra characters beyond the expected, the only 
    # characters remaining should be numbers (0-9), white space (\s), > and .
    # for decimal points
    line = re.sub(r'[^0-9\s><.]+', '', line)
    return line

def checkDecimalPoints(line):
    length = len(line)
    for i in range(1, length - 1):
        prevChar = line[i - 1]
        currChar = line[i]
        nextChar = line[i + 1]

        if ((currChar is '.') and 
            (not prevChar.isdigit()) and 
            (not nextChar.isdigit())):

            line = line[0: i] + line[i + 1:]
    
    return line
    
def isValidLength(line):
    line = line.strip
    parts = line.split()
    return (len(parts) is 4)

def getNumericalValues(text, tableType):
    startingVal, endingVal = rawScoreValues(tableType)
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
    
    return firstLine, lastLine

def rawScoreValues(tableType):
    startingVal = None
    endingVal = None
    rawScores = {'verbal1': [108, 52], 
                        'verbal2': [51, 0],
                        'nonverbal': [46, 0]}
    
    for key in rawScores:
        if key is tableType:
            startingVal = rawScores[key][0]
            endingVal = rawScores[key][1]
    
    return startingVal, endingVal
    
def createDataFrame(tableType):
    startingVal, endingVal = rawScoreValues(tableType)
    rawScores = list(range(startingVal, endingVal - 1, -1)) # Because always these values
    df = pd.DataFrame({'Raw': rawScores})
    df.set_index('Raw', inplace = True) # Removes 0-index, makes raw score new index
    return df

def listToDataFrame(list, tableType, ):
    df = createDataFrame(tableType)
    cleanedData = pd.DataFrame(list)
    cleanedData.set_index('Raw', inplace=True)
    df = df.join(cleanedData)
    return df

def dataFrameToCSV(df, tableType, outputFolder):
    fileName = 'kbit2_test.csv'
    filePath = os.path.join(outputFolder, fileName)

    df.to_csv(filePath)
    print(f'Saved {fileName} to {filePath}')