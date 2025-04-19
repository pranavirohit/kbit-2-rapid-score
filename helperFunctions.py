import cv2
import pytesseract as pyt

def processImage(filePath):
    image = cv2.imread(filePath)
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold = (grayImage, 150, 255, cv2.THRESH_BINARY_INV)
    processedImage = threshold[1]

    return processedImage

def extractAllText(image):
    text = pyt.image_to_string(image, config = '--psm 6')
    return text