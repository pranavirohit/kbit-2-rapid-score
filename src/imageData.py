from commonImports import *

testPage = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\data_files\page_78.png"
verbalTest, nonVerbalTest = splitImage(testPage)

verbalProcessed = processImage(verbalTest)
nonVerbalProcessed = processImage(nonVerbalTest)
print(extractAllText(verbalProcessed))
print(extractAllText(nonVerbalProcessed))


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

def getVerticalLinesPositions(filePath):
  threshold = thresholdImage(filePath)
  # Tutorial: https://www.youtube.com/watch?v=E_NRYxJyZlg
  # Used this tutorial for an introduction to isolating elements in
  # OpenCV, then came up with a similar algorithm for my own elements
  # with vertical lines

  # See my logbook entry for my notes on the tutorial, and how I generated
  # the algorithm for isolating the vertical lines


  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 50))
  # getStructuringElement(shape, (width, height))

  verticalLines = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)

  
def thresholdImage(filePath):
  # Read in image and turn into grayscale version
  image = cv2.imread(filePath, 0)
  grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Generates an image with a black background, white lines and text
  # This is called thresholding, which gives us the mask
  _, binaryImage = cv2.threshold(array, 150, 255, cv2.THRESH_BINARY_INV)
  return binaryImage
