'''
Used ChatGPT to reformat all lines to < 80 characters.
No changes to the actual code structure were made.
'''
from commonImports import *

# Input: File path for the image with the CSV images
# Output: String with values extracted before cleaning
def extractAllText(filePath):
    image = PILImage.open(filePath)
    text = pyt.image_to_string(image, config='--psm 6')
    return text

# Input: String with values extracted before cleaning
# Output: List of dictionaries, turns each line into a dictionary in the format 
# {'Raw': , 'Standard': , 'ConfidenceInterval': , 'Percentile': }

def cleanTextToList(text, tableType):
    cleanedData = createEmptyDataList(tableType)
    lastUpdatedRawScore = None

    allLines = text.splitlines()
    firstLine, lastLine = getNumericalValues(text, tableType) 
    selectedLines = allLines[firstLine: lastLine]

    for line in selectedLines:
        line = line.strip()
        line = cleanLine(line)
        parts = reformatParts(line)
        parts = fillInMissingValues(parts, lastUpdatedRawScore)
        print(parts)

        # Changed to update pre-made dictionary, based on fixed raw scores
        lastUpdated = updateDictionary(line, parts, cleanedData)
        if lastUpdated is not None:
            lastUpdatedRawScore = lastUpdated

    print(cleanedData)
    return cleanedData

def fillInMissingValues(parts, lastUpdated):
    if len(parts) == 3:
        parts = placeholderRawScore(parts, lastUpdated)
    return parts

def placeholderRawScore(parts, lastUpdated):
    potentialRange = parts[1]
    if potentialRange.find('-') != -1:
        parts.insert(0, str(lastUpdated - 1)) 
    return parts

def createEmptyDataList(tableType):
    toPopulate = []
    startingVal, endingVal = rawScoreValues(tableType)
    for i in range(startingVal, endingVal - 1, -1):
        row = {
            'Raw': i,
            'Standard': None,
            'ConfidenceInterval': None,
            'Percentile': None
        }
        toPopulate.append(row)
    return toPopulate

def reformatParts(line):
    parts = line.split()
    result = []
    for part in parts:
        part = part.strip()
        part = checkDecimalPoints(part)
        # Remove unwanted characters, keep digits, whitespace, etc.
        part = re.sub(r'[^0-9\s><.-]+', '', part)
        if part != '':
            result.append(part)
    return result

def updateDictionary(line, parts, dataList):
    try: 
        rawScore = int(parts[0])
        standScore = int(parts[1])
        confInt = parts[2]
        if confInt.count('-') > 1:
            rawScore, confInt = checkConfidenceInterval(confInt)
        percentile = checkPercentile(parts[3])
        for valDict in dataList:
            if valDict['Raw'] == rawScore:
                valDict['Raw'] = rawScore
                valDict['Standard'] = standScore
                valDict['ConfidenceInterval'] = confInt
                valDict['Percentile'] = percentile
                return rawScore
    except:
        print(f'Skipping line (parse error): {line}')
        return None

def checkPercentile(part):
    if len(part) == 5:
        return '>99.9'
    return part

def checkConfidenceInterval(part):
    values = part.split('-')
    updatedRawScore = int(values[0])
    updatedConfInt = f'({values[1]}-{values[2]})'
    return updatedRawScore, updatedConfInt

def getOnlyDigits(line):
    firstDigit = None
    lastDigit = None
    length = len(line)
    for i in range(length):
        if line[i].isdigit() and firstDigit is None:
            firstDigit = i
    for i in range(length - 1, -1, -1):
        if line[i].isdigit() and lastDigit is None:
            lastDigit = i
    if firstDigit is None and lastDigit is None:
        print(f'Error in finding digit values: {line}')
        return line
    return line[firstDigit: lastDigit + 1]

def cleanLine(line):
    line = getOnlyDigits(line)
    line = line.replace('|', ' ')
    line = line.replace('_', ' ')
    line = line.replace('—', '-')
    line = line.replace('=', ' ')
    return line.strip()

def checkDecimalPoints(part):
    if part.startswith('.'):
        part = part[1:]
    if part.endswith('.'):
        part = part[:-1]
    return part

def isValidLength(line):
    line = line.strip()
    parts = line.split()
    return len(parts) == 4

def getNumericalValues(text, tableType):
    startingVal, endingVal = rawScoreValues(tableType)
    currLine = 0
    firstLine = None
    lastLine = None
    for line in text.splitlines():
        line = line.strip()
        if line.startswith(str(startingVal)):
            firstLine = currLine
        if 'B.1' in line and firstLine is not None:
            lastLine = currLine
            return firstLine, lastLine
        currLine += 1
    return firstLine, lastLine

def rawScoreValues(tableType):
    rawScores = {
        'verbal1': [108, 52], 
        'verbal2': [51, 0],
        'nonverbal': [46, 0]
    }
    return rawScores.get(tableType, [None, None])

def createDataFrame(tableType):
    startingVal, endingVal = rawScoreValues(tableType)
    rawScores = list(range(startingVal, endingVal - 1, -1))
    df = pd.DataFrame({'Raw': rawScores})
    df.set_index('Raw', inplace=True)
    return df

# Input: List of dictionaries, where each dictionary represents the values on
# each line, {'Raw': , 'Standard': , 'ConfidenceInterval': , 'Percentile' 
# Output: Data frame with columns 'Raw', 'Standard', 'ConfidenceInterval', 
# 'Percentile'
def listToDataFrame(dataList, tableType):
    df = createDataFrame(tableType)
    cleanedData = pd.DataFrame(dataList)
    cleanedData.set_index('Raw', inplace=True)
    return df.join(cleanedData)

# Input: Data frame
def dataFrameToCSV(df, tableType, pageNum, outputFolder):
    fileName = f'{tableType}_page_{pageNum}.csv'
    filePath = os.path.join(outputFolder, fileName)
    os.makedirs(outputFolder, exist_ok=True)
    # Added index=False to avoid duplicating raw score column
    df.to_csv(filePath, index=False)
    print(f'Saved {fileName} to {filePath}')
