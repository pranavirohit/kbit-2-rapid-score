# from [fileName] import [functionName]
import cv2 # OpenCV
import pytesseract as pyt # Tesseract
from cmu_graphics import* # CMU graphics
from pdf2image import convert_from_path #PDF2Image
import os

from helperFunctions import *

# def loopThroughAllFiles(folderPath):
#     for fileName in os.listdir(folderPath, fileName):
#         fullPath = os.path.join(folderPath, fileName)

#         if os.path.isfile(fullPath):

testPage = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\data_files\page_78.png"
verbalTest, nonVerbalTest = splitImage(testPage)

verbalProcessed = processImage(verbalTest)
nonVerbalProcessed = processImage(nonVerbalTest)
print(extractAllText(verbalProcessed))

print(extractAllText(nonVerbalProcessed))

# processed = processImage(testPage)
# test = extractAllText(processed)
# print(test)

