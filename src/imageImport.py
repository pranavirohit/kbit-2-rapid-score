# from [fileName] import [functionName]
import cv2 # OpenCV
import pytesseract as pyt # Tesseract
from cmu_graphics import* # CMU graphics
from pdf2image import convert_from_path #PDF2Image

from helperFunctions import *

# Test page
scannedKBIT = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\starter_files\KBIT_Pages_78_84.pdf"
# Save images here
allKBITimages = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\data_files"

processPDF(scannedKBIT, allKBITimages)