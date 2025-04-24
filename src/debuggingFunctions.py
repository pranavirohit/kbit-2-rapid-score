'''
Used ChatGPT to reformat all lines to < 80 characters.
No changes to the actual code structure were made.
'''
from commonImports import *

def onAppStart(app):
    app.filePath = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\data_files\page_78.png"
    app.rectangles = getVerticalLinesPositions(app.filePath)

def redrawAll(app):
    drawImage(app.filePath, 0, 0)
    
    for left, top, width, height in app.rectangles:
        print(left)
        lineWidth = 10
        drawRect(left, top, lineWidth, height, fill = 'red')
        
runApp()