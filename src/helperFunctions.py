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

import cv2
import pytesseract as pyt
from pdf2image import convert_from_path #PDF2Image
from PIL import Image
import os


def splitImage(filePath):
    # Read in image and turn into grayscale version
    image = cv2.imread(filePath)
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Locate where to split image so I can process the Nonverbal Table and Verbal Table seperately
    height, width = grayImage.shape
    splitCol = int(width * (2/3))

    # gray[rows, cols]
    verbalArray = grayImage[:, 0:splitCol] # Process all rows, but stop at the midpoint column
    nonVerbalArray = grayImage[:, splitCol:] # Process all rows, but START at the midpoint column

    return verbalArray, nonVerbalArray

def processImage(array):
    _, binaryImage = cv2.threshold(array, 150, 255, cv2.THRESH_BINARY_INV)
    processedImage = Image.fromarray(binaryImage)

    return processedImage

def extractAllText(image):
    
    text = pyt.image_to_string(image, config = '--psm 6')
    return text

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

# Want to eventually name the Table B1 files by their age
def getTableAge(image):
    pass