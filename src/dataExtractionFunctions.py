from commonImports import *

def extractAllText(filePath):
    image = PILImage.open(filePath)
    text = pyt.image_to_string(image, config='--psm 6')
    return text

def cleanTextToList(text, tableType):
    cleanedData = []
    allLines = text.splitlines()
    firstLine, lastLine = getNumericalValues(text, tableType) 

    # Added type check (recommended by ChatGPT)
    if firstLine is None or lastLine is None:
        print(f"Warning: couldn't find bounds for {tableType}")
        return []

    selectedLines = allLines[firstLine: lastLine]

    for line in selectedLines:
        line = line.strip()
        line = re.sub(r'[^0-9\s><.-]+', '', line)
        # line = cleanLine(line)

        
        # line = line.strip()
        parts = reformatParts(line)

        if len(parts) == 3:
            parts = addRawScore(parts)

        values = createDictionary(line, parts)

        if values is not None:
            cleanedData.append(values)
    
    print(cleanedData)
    return cleanedData

def addRawScore(parts):
    potentialRange = parts[1]
    if (potentialRange.find('-') != -1):
        parts.insert(0, '0') # Insert 0 as a placeholder value for the
        # index
        return parts
    
def reformatParts(line):
    parts = line.split()
    result = []

    for part in parts:
        part = part.strip()
        part = checkDecimalPoints(part)
        part = re.sub(r'[^0-9\s><.-]+', '', part)

        if part != '':
            result.append(part)
    
    return result

def createDictionary(line, parts):
    try: 
        rawScore = int(parts[0])
        standScore = int(parts[1])
        confInt = parts[2]
        percentile = checkPercentile(parts[3])

        result = ({
            'Raw': rawScore,
            'Standard': standScore,
            'ConfidenceInterval': confInt,
            'Percentile': percentile
        })
        return result
    
    except:
        print(f'Skipping line (parse error): {line}')
        return None

def checkPercentile(part):
    if len(part) == 4:
        return '>99.9'
    else:
        return part
    
def getOnlyDigits(line):
    firstDigit = None
    lastDigit = None
    length = len(line)

    for i in range(length):
        char = line[i]
        if char.isdigit() and firstDigit is None:
            firstDigit = i
    
    for i in range(length - 1, -1, -1):
        char = line[i]
        if char.isdigit() and lastDigit is None:
            lastDigit = i
    
    if firstDigit is None and lastDigit is None:
        print(f'Error in finding digit values: {line}')
        return line
    
    line = line[firstDigit: lastDigit + 1]
    return line

# def cleanLine(line):
#     line = getOnlyDigits(line)
#     line = line.replace('|', ' ')
#     line = line.replace('_', ' ')
#     line = line.replace('—', '-')
#     line = line.replace('=', ' ')
#     lin

#     # Tutorial: https://www.w3schools.com/python/python_regex.asp
#     # Checks replaces any extra characters beyond the expected, the only 
#     # characters remaining should be numbers (0-9), white space (\s), > and .
#     # for decimal points
#     return line

def checkDecimalPoints(part):
    if part.startswith('.'):
        part = part[1:]
    if part.endswith('.'):
        part = part[-1]
    return part

    # # Changed to while loop from for loop to keep track of indices
    # i = 1 
    # length = len(line)
    # while i < (length - 1):
    #     prevChar = line[i - 1]
    #     currChar = line[i]
    #     nextChar = line[i + 1]

    #     if (currChar == '.'):
    #         if ((i == 0) or 
    #             (i == length - 1)):
                
    #             line = line[0: i] + line[i + 1:]
       
    #     else:
    #         i += 1
    
    # return line

def isValidLength(line):
    line = line.strip()
    parts = line.split()
    return (len(parts) == 4)

def getNumericalValues(text, tableType):
    startingVal, endingVal = rawScoreValues(tableType)
    currLine = 0
    firstLine = None
    lastLine = None
    
    for line in text.splitlines():
        line = line.strip()
        
        # Added string comparison (recommended by ChatGPT)
        if line.startswith(str(startingVal)):
            firstLine = currLine
        
        if 'B.1' in line and firstLine is not None:
            lastLine = currLine
            return firstLine, lastLine
        
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
    rawScores = list(range(startingVal, endingVal - 1, -1))
    df = pd.DataFrame({'Raw': rawScores})
    df.set_index('Raw', inplace=True)
    return df

def listToDataFrame(dataList, tableType):
    df = createDataFrame(tableType)
    cleanedData = pd.DataFrame(dataList)
    cleanedData.set_index('Raw', inplace=True)
    df = df.join(cleanedData)
    return df

def dataFrameToCSV(df, tableType, outputFolder):
    fileName = f'kbit2_{tableType}.csv'
    filePath = os.path.join(outputFolder, fileName)
    
    # Added folder existence check (recommended by ChatGPT)
    os.makedirs(outputFolder, exist_ok=True)

    df.to_csv(filePath)
    print(f'Saved {fileName} to {filePath}')