'''
KBIT-2 Visual Line Debugger

This file opens a KBIT-2 test page and overlays red rectangles on top of all
the vertical lines detected by getVerticalLinesPositions(). It's meant to be
a quick visual check to confirm if the line detection is working properly, as
I wasn't getting the expected 9 vertical lines.

→ Requires CMU Graphics + my helper functions in commonImports.py

'''

from commonImports import *

def onAppStart(app):
    app.filePath = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\data_files\page_78.png"
    app.rectangles = getVerticalLinesPositions(app.filePath)

def redrawAll(app):
    drawImage(app.filePath, 0, 0)
    
    for i in range(len(app.rectangles)):
        (left, top, width, height) = app.rectangles[i]
        print(left)
        drawRect(left, top, 10, height, fill = 'red')
        
runApp()