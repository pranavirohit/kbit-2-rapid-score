from commonImports import *

def onAppStart(app):
    app.filePath = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\data_files\page_78.png"
    app.rectangles = getVerticalLinesPositions(app.filePath)

def redrawAll(app):
    drawImage(app.filePath, 0, 0)
    for i in range(len(app.rectangles)):
        (left, top, width, height) = app.rectangles[i]
        drawRect(left, top, width, height, fill = 'red')
        
cmu_graphics.run()