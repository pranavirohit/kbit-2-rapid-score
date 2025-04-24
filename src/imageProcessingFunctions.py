from commonImports import *

def processPDF(pdfPath, pageOutputFolder, tableOutputFolder):
    # Reduced dpi to 200 to bound PNG size, as dpi = 300 was too large
    images = convert_from_path(pdfPath, dpi = 200)
    
    for index, image in enumerate(images):
        bookStartingPage = 78 # Corresponds to physical book
        pageNum = index + bookStartingPage
        fileName = f'page_{pageNum}.png'

        fullPagePath = os.path.join(pageOutputFolder, fileName)
        image.save(fullPagePath, 'PNG')

        print(f'Added {fileName} to {fullPagePath}')

        saveTablesFromPage(fullPagePath, tableOutputFolder, pageNum)


def saveTablesFromPage(filePath, tableOutputFolder, pageNum):
    linePos = getVerticalLinesPositions(filePath)
    verbal1image, verbal2image, nonverbalImage = splitThreeTables(filePath, linePos)

    verbal1Path = os.path.join(tableOutputFolder, f"verbal1_page_{pageNum}.png")
    verbal2Path = os.path.join(tableOutputFolder, f"verbal2_page_{pageNum}.png")
    nonverbalPath = os.path.join(tableOutputFolder, f"nonverbal_page_{pageNum}.png")

    verbal1image.save(verbal1Path, 'PNG')
    verbal2image.save(verbal2Path, 'PNG')
    nonverbalImage.save(nonverbalPath, 'PNG')

    print(f'Saved cropped tables for page {pageNum} to {tableOutputFolder}')

def splitImage(filePath):
    image = cv2.imread(filePath, 0)
    height, width = image.shape
    splitCol = int(width * (2/3))
    verbalArray = image[:, 0:splitCol] # Process all rows, but stop at the midpoint column
    nonVerbalArray = image[:, splitCol:] # Process all rows, but START at the midpoint column

    return verbalArray, nonVerbalArray

def processImage(array):
    _, binaryImage = cv2.threshold(array, 150, 255, cv2.THRESH_BINARY_INV)
    processedImage = PILImage.fromarray(binaryImage)

    return processedImage

def getTableAge(image):
    pass

# See my notes on algorithm development in logbook.txt
def getVerticalLinesPositions(filePath):
    imgThreshold = thresholdImage(filePath)
    imgLinesOnly = isolateVerticalLines(imgThreshold)

    lines, _ = cv2.findContours(imgLinesOnly, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    positions = []
    for line in lines:
        left, top, width, height = cv2.boundingRect(line)
        rectInfo = (left, top, width, height)
        if height > 100:  # Filter out small noise
            positions.append(rectInfo)

    return sorted(positions)


def thresholdImage(filePath):
    image = cv2.imread(filePath, 0)
    _, binaryImage = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)
    return binaryImage


def isolateVerticalLines(image):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 50))
    verticalLines = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    return verticalLines

def getXCoordinate(positions):
    result = []
    for left, top, width, height in positions:
        result.append(left)
    return result
    
def splitThreeTables(filePath, linePos):
    xCoordinates = getXCoordinate(linePos)
    image = cv2.imread(filePath, 0)

    x0 = xCoordinates[0]
    x2 = xCoordinates[2]
    x3 = xCoordinates[3]
    x5 = xCoordinates[5]
    x6 = xCoordinates[6]
    x8 = xCoordinates[8]

    verbal1left = x0
    verbal2left = verbal1right = findMidpoint(x2, x3)

    nonverbal1left = verbal2right = findMidpoint(x5, x6)
    nonverbal2right = x8

    verbal1Array = image[:, verbal1left: verbal1right]
    verbal2Array = image[:, verbal2left: verbal2right]
    nonverbalArray = image[:, nonverbal1left: nonverbal2right]

    verbal1image = processImage(verbal1Array)
    verbal2image = processImage(verbal2Array)
    nonverbalImage = processImage(nonverbalArray)

    return verbal1image, verbal2image, nonverbalImage

def findMidpoint(line1, line2):
    return (line1 + line2) // 2