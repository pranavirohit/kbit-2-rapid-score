import cv2
import pytesseract as pyt
from pdf2image import convert_from_path #PDF2Image
import os

def processImage(filePath):
    image = cv2.imread(filePath)
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold = (grayImage, 150, 255, cv2.THRESH_BINARY_INV)
    processedImage = threshold[1]

    return processedImage

def extractAllText(image):
    text = pyt.image_to_string(image, config = '--psm 6')
    return text

def processPDF(pdfPath, outputFolder):
    # Convert each PDF page to an image
    images = convert_from_path(pdfPath, dpi = 300)

    # Save each image to the specified output folder by 
    for index, image in enumerate(images):
        # age = getTableAge(image)
        
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