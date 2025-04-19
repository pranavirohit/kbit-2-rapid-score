import cv2 # OpenCV
import os
import pytesseract as pyt # Tesseract

from cmu_graphics import* # CMU graphics
from pdf2image import convert_from_path #PDF2Image
from helperFunctions import *

testPage = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\data_files\page_78.png"
verbalTest, nonVerbalTest = splitImage(testPage)

verbalProcessed = processImage(verbalTest)
nonVerbalProcessed = processImage(nonVerbalTest)
print(extractAllText(verbalProcessed))
print(extractAllText(nonVerbalProcessed))

