# from [fileName] import [functionName]
import cv2 # Importing OpenCV
import pytesseract # Importing Tesseract
from cmu_graphics import* # Importing CMU graphics

def testOpenCV():
    print(f'OpenCV test: {cv2.__version__}')

def testTesseract():
    print(f'Tesseract test: {pytesseract.get_tesseract_version()}')

def onAppStart(app):
    app.radius = 20
    app.width, app.height = 200, 200

def redrawAll(app):
    drawCircle(app.width / 2, app.height / 2, app.radius, fill = 'cyan')

def main():
    runApp()
main()



