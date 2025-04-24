'''
KBIT-2 Text Extraction and Cleaning Helpers

This file has the main functions I'm using to extract, clean, and structure 
table data from the KBIT-2 scoring pages after OCR. The goal is to go from 
messy OCR output to a clean list of rows that can be saved as a CSV.

Each function helps clean and parse the values from scanned table images, 
especially handling edge cases like missing raw scores, weird formatting 
of confidence intervals, and OCR misreads. I developed each function after
looking through the outputs and recognizing common patterns in errors. See 
my logbook for my notes on this.  

Here's what each function does and how I built them:

- extractAllText(image):
    OCR pass using Tesseract, with PSM 6 (treats it like a single block of text).
    Works best after thresholding. Decided on PSM 6 because of information below.
    → https://github.com/tesseract-ocr/tesseract/blob/main/doc/tesseract.1.asc#options

- cleanTextToList(text, tableType):
    Main function for turning OCR output into a cleaned list of dictionaries. 
    Finds the lines that matter, splits each into parts, handles missing values, 
    and fills in a pre-built dictionary for each raw score.

- fillInMissingValues(parts, lastUpdated):
    If a line is missing the raw score (common after OCR), this fills it in 
    based on the last seen value. Uses placeholderRawScore to insert the fix.

- placeholderRawScore(parts, lastUpdated):
    Inserts a raw score value that's one less than the last updated one. 
    Used to fix rows where OCR missed the raw score entirely.

- updateDictionary(line, parts, dataList):
    Tries to parse the 4 expected values (raw score, standard score, CI, percentile)
    and match them to the right row in the pre-built dictionary. Handles edge cases 
    like when raw score is accidentally stuck to the confidence interval.

- createEmptyDataList(tableType):
    Creates a full list of dictionaries for each expected raw score (depending on 
    table type). These get filled in later by updateDictionary, as the rows are read
    in from the file with OCR.

- reformatParts(line):
    Splits a cleaned line into individual score values. Applies checkDecimalPoints 
    and uses regex to remove unexpected OCR characters — keeping only digits (0–9), 
    whitespace (\s), dots (.), and greater-than signs (>).
    → https://www.w3schools.com/python/python_regex.asp

- cleanLine(line):
    Does a first pass at cleaning. Strips extra characters like pipes, underscores, 
    or long dashes, and isolates just the digits.

- getNumericalValues(text, tableType):
    Finds which lines in the OCR text actually contain the table values. 
    Returns the start and end index so we can extract only the useful part.
    → Recommended by ChatGPT: String conversion as one of the checks 

- checkConfidenceInterval(part):
    Deals with lines where the raw score and confidence interval were joined.
    Extracts both cleanly.

- checkPercentile(part):
    Fixes the special case where the percentile is OCR'd as a 5-character string 
    like '9999>' or '99.9>' and returns it as '>99.9'.

- checkDecimalPoints(part):
    Fixes common OCR issues where decimals get cut off at the beginning or end.

- isValidLength(line):
    Checks whether a line has exactly 4 parts (the expected number). Used 
    to help catch bad OCR rows.

- rawScoreValues(tableType):
    Returns the expected raw score range for the given table type 
    ('verbal1', 'verbal2', 'nonverbal').

- createDataFrame(tableType):
    Builds a Pandas DataFrame with raw scores as the index, to match later 
    with cleaned data.
    → https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html

- listToDataFrame(dataList, tableType):
    Joins the cleaned list of score data with a raw-score-indexed DataFrame.
    → https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html
    → https://pandas.pydata.org/docs/user_guide/merging.html#joining-on-index
    
- dataFrameToCSV(df, tableType, pageNum, outputFolder):
    Saves the final cleaned DataFrame to a CSV in the output folder. 
    Automatically creates the folder if it doesn't exist.
    → Recommended by ChatGPT: Check that folder exists

'''
from commonImports import *

def extractAllText(filePath):
    image = PILImage.open(filePath)
    text = pyt.image_to_string(image, config='--psm 6')
    return text

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
        if lastUpdated != None:
            lastUpdatedRawScore = lastUpdated
    
    print(cleanedData)
    return cleanedData

def fillInMissingValues(parts, lastUpdated):
    if len(parts) == 3:
            # print(f'parts: {parts}, lastUpdated: {lastUpdated}')
            parts = placeholderRawScore(parts, lastUpdated)
            # print(f'after parts: {parts}, lastUpdated: {lastUpdated}')
    return parts

def placeholderRawScore(parts, lastUpdated):
    potentialRange = parts[1]
    if (potentialRange.find('-') != -1):
        parts.insert(0, str(lastUpdated - 1)) 
        return parts

def createEmptyDataList(tableType):
    toPopulate = []
    startingVal, endingVal = rawScoreValues(tableType)
    for i in range(startingVal, endingVal - 1, -1):
        row = ({
        'Raw': i,
        'Standard': None,
        'ConfidenceInterval': None,
        'Percentile': None,
        })
        toPopulate.append(row)
    
    return toPopulate
    
def reformatParts(line):
    parts = line.split()
    result = []

    for part in parts:
        part = part.strip()
        part = checkDecimalPoints(part)
        
        # Tutorial: https://www.w3schools.com/python/python_regex.asp
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
    else:
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

def cleanLine(line):
    line = getOnlyDigits(line)
    line = line.replace('|', ' ')
    line = line.replace('_', ' ')
    line = line.replace('—', '-')
    line = line.replace('=', ' ')
    line = line.strip()

    return line

def checkDecimalPoints(part):
    if part.startswith('.'):
        part = part[1:]
    if part.endswith('.'):
        part = part[:-1]
    return part

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
    
    # Tutorial: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html
    df.set_index('Raw', inplace=True)
    return df

def listToDataFrame(dataList, tableType):
    df = createDataFrame(tableType)
    cleanedData = pd.DataFrame(dataList)

    # Tutorial: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html
    cleanedData.set_index('Raw', inplace=True)
    df = df.join(cleanedData)
    
    return df

def dataFrameToCSV(df, tableType, pageNum, outputFolder):
    fileName = f'{pageNum}_{tableType}.csv'
    filePath = os.path.join(outputFolder, fileName)
    
    # Added folder existence check (recommended by ChatGPT)
    os.makedirs(outputFolder, exist_ok=True)

    df.to_csv(filePath)
    print(f'Saved {fileName} to {filePath}')