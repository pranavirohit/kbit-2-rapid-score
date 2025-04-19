"""
This file has the main helper functions I'm using to automate KBIT-2 scoring.

- processImage(filePath):
  Takes in the path to an image file, converts it to grayscale using OpenCV,
  applies binary thresholding (to help Tesseract read it better), and returns 
  the processed image as a PIL object so it's compatible with Tesseract OCR.

- extractAllText(image):
  Takes in a PIL image and uses Tesseract to extract all text from it.
  Right now it's using page segmentation mode 6 (treats the image as a block of text).

- processPDF(pdfPath, outputFolder):
  Takes a scanned PDF (like the scoring tables from the KBIT-2 manual),
  converts each page to an image (using pdf2image), and saves each one 
  as a PNG in the specified folder. Right now I'm hardcoding the first page 
  to be page 78 since that's where Table B.1 starts in the book.

- getTableAge(image):
  Placeholder function I want to build later — goal is to detect the 
  age range from each scoring table page and use it to name the files in a way that's
  more meaningful.
"""
from commonImports import *

def processPDF(pdfPath, outputFolder):
    # Convert each PDF page to an image
    images = convert_from_path(pdfPath, dpi = 300)

    # Save each image to the specified output folder by 
    for index, image in enumerate(images):
        bookStartingPage = 78 # Corresponds to physical book
        pageNum = index + bookStartingPage
        fileName = f'page_{pageNum}.png'

        # Specify path to save image
        fullPath = os.path.join(outputFolder, fileName)
        image.save(fullPath, 'PNG') # Use Pillow for this

        print(f'Added {fileName} to {fullPath}')


def splitImage(filePath):
    # Read in image and turn into grayscale version
    image = cv2.imread(filePath, 0)
    
    # Locate where to split image so I can process the Nonverbal Table and Verbal Table seperately
    height, width = image.shape
    splitCol = int(width * (2/3))

    # gray[rows, cols]
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

# Want to eventually name the Table B1 files by their age
def getTableAge(image):
    pass

'''
### Splitting Image to Extract Table Data
1. Assuming I have a PNG of the table file, I want to split it into the three
tables on the page. I plan to do this by looking for vertical lines:

Verbal (Table 1):
Start Line: 1, End Line: 3

Verbal (Table 2):
Start Line: 4, End Line: 6

Nonverbal (Table 3):
Start Line: 7, End Line: 9

2. Then, I want to find the location for each of the vertical lines
3. Using the location for each, I want to create three new PNGs, store
them in a new folder
4. Then, I want to create an algorithm to extract the text from 
each of these pages. This is easier, because it's just recognizing
the same four columns and turning it into a data structure I can run this
on all the images for.
'''

# Tutorial: https://www.youtube.com/watch?v=E_NRYxJyZlg
# Used this tutorial for an introduction to isolating elements in
# OpenCV, then came up with a similar algorithm for my own elements
# with vertical lines

# See my logbook entry for my notes on the tutorial, and how I generated
# the algorithm for isolating the vertical lines

def getVerticalLinesPositions(filePath):
  imgThreshold = thresholdImage(filePath)
  imgLinesOnly = isolateVerticalLines(imgThreshold)

  # cv2.findContours(image, mode, method)
  lines, _ = cv2.findContours(imgLinesOnly, cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_NONE)
  positions = []
  for line in lines:
    # Get dimensions of line (which is stored as a rectangle)
    left, top, width, height = cv2.boundingRect(line)
    rectInfo = (left, top, width, height)
    positions.append(rectInfo)
  
  return sorted(positions)

def thresholdImage(filePath):
  # Read in image and turn into grayscale version
  image = cv2.imread(filePath, 0)

  # Generates an image with a black background, white lines and text
  # This is called thresholding, which gives us the mask
  _, binaryImage = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)
  return binaryImage

def isolateVerticalLines(image):
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 50))
  # getStructuringElement(shape, (width, height))
  verticalLines = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
  return verticalLines

