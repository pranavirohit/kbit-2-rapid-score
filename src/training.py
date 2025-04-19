# from [fileName] import [functionName]

# Importing OpenCV
import cv2
print(f'OpenCV test: {cv2.__version__}')

import pytesseract

# Importing CMU graphics
from cmu_graphics import*

def onAppStart(app):
    app.radius = 20
    app.width, app.height = 200, 200

def redrawAll(app):
    drawCircle(app.width / 2, app.height / 2, app.radius, fill = 'cyan')

def main():
    print(f'Tesseract test: {pytesseract.get_tesseract_version()}')
    runApp()

main()

# Importing Tesseract


