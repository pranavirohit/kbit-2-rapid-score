'''
KBIT-2 Table Processing Helpers

This file has the main helper functions I'm using to automate KBIT-2 scoring.
With these functions, I want to turn a scanned PDF of KBIT-2 scoring pages into 
clean, labeled PNGs, to isolate just the columns I need and running OCR on them.

Right now, here's what each function does and where I learned how to build them:

- processPDF(pdfPath, outputFolder):
    Converts each page of the scanned KBIT-2 PDF into a high-res PNG.
    It starts from page 78 (based on the book) and saves each image
    into a folder so I can process them later.
    → https://pypi.org/project/pdf2image/
    → https://pillow.readthedocs.io/en/stable/reference/Image.html

- splitImage(filePath):
    Splits the page into Verbal and Nonverbal tables by column.
    I assume a 2:1 layout ratio for now — just enough for early testing.
    This function will be replaced by the splitThreeTables(filePath, linePos)
    function which I am currently working on.

- processImage(array):
    Takes a NumPy array (grayscale) and applies binary thresholding
    to help Tesseract read it more cleanly. Converts back to a PIL image
    so Tesseract can process this. I used this for the initial text extraction,
    which I'm now refining with more recent helper functions.
    → https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html

- extractAllText(image):
    OCR pass using Tesseract, with PSM 6 (treats it like a single block of text).
    Works best after thresholding. Decided on PSM 6 because of information below.
    → https://github.com/tesseract-ocr/tesseract/blob/main/doc/tesseract.1.asc#options

- getTableAge(image):
    Placeholder — I want this to eventually detect age ranges (like 6:0–6:11)
    so the files are more searchable by range.

- getVerticalLinesPositions(filePath):
    Isolates all the vertical lines in the image and returns their bounding boxes
    as (left, top, width, height). Will use these to crop specific tables next.
    → https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html
    → Tutorial I adapted this from: https://youtu.be/E_NRYxJyZlg
    → See my notes on algorithim development in logbook.txt

- thresholdImage(filePath):
    Just converts an image into black/white (inverted) using thresholding.
    This creates the binary mask that helps us isolate lines.
    → https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html

- isolateVerticalLines(image):
    Uses a vertical kernel to extract only the vertical lines using 
    morphological operations (OpenCV's morphologyEx with a tall filter).
    → https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html

- splitThreeTables(filePath, linePos):
    Crops the full PNG image into three separate table images:
    Verbal Table 1, Verbal Table 2, and Nonverbal Table.
    Uses midpoints between vertical line positions to crop columns,
    then processes each cropped region for OCR. Assumes linePos has 
    at least 9 sorted x-coordinates, mapped to each of the 9 vertical
    lines in the original table.
    → This will eventually replace splitImage() with more accurate cropping.

'''

from commonImports import *

def processPDF(pdfPath, outputFolder):
    images = convert_from_path(pdfPath, dpi = 300)
    
    for index, image in enumerate(images):
        bookStartingPage = 78 # Corresponds to physical book
        pageNum = index + bookStartingPage
        fileName = f'page_{pageNum}.png'

        fullPath = os.path.join(outputFolder, fileName)
        image.save(fullPath, 'PNG')

        print(f'Added {fileName} to {fullPath}')


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

def extractAllText(image):
    text = pyt.image_to_string(image, config = '--psm 6')
    return text

def getTableAge(image):
    pass

# See my notes on algorithim development in logbook.txt
def getVerticalLinesPositions(filePath):
  imgThreshold = thresholdImage(filePath)
  imgLinesOnly = isolateVerticalLines(imgThreshold)

  lines, _ = cv2.findContours(imgLinesOnly, cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_NONE)
  
  positions = []
  for line in lines:
    left, top, width, height = cv2.boundingRect(line)
    rectInfo = (left, top, width, height)
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

def splitThreeTables(filePath, linePos):
   image = cv2.imread(filePath, 0)
  
  # Might come back and change x0 = linePos[0], etc. so it's more readable
   verbal1left = linePos[0]
   verbal2left = verbal1right = findMidpoint(linePos[2], linePos[3])
   nonverbal1left = verbal2right = findMidpoint(linePos[5], linePos[6])
   nonverbal2right = linePos[8]

   verbal1Array = image[:, verbal1left:verbal1right]
   verbal2Array = image[:, verbal2left:verbal2right]
   nonverbalArray = image[:, nonverbal1left:nonverbal2right]
   
   verbal1image = processImage(verbal1Array)
   verbal2image = processImage(verbal2Array)
   verbal3image = processImage(nonverbalArray)
   
   return verbal1image, verbal2image, verbal3image 
          
def findMidpoint(line1, line2):
   return line1 + line2 // 2
