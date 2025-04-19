import cv2

def processImage(filePath):
    image = cv2.imread(filePath)
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold = (grayImage, 150, 255, cv2.THRESH_BINARY_INV)
    finalImage = threshold[1]

    return finalImage

