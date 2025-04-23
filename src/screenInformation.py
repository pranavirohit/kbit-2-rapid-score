from commonImports import *

screenNames = ['start', 'info', 'template', 'upload', 'output1',
               'output2', 'output3', 'results', 'end' ]

def onAppStart(app):
    app.filePath = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\KBIT_2_Start_Screen.png"
    app.width, app.height = 960, 540
    app.cx, app.cy = app.width // 2, app.height // 2
    app.buttonCenters = []

def start_redrawAll(app):
    image = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\KBIT_2_Start_Screen.png"
    drawImage(image, app.cx, app.cy, align = 'center')
    rectCy, rectWidth, rectHeight = 400, 300, 40
    # drawRect(app.cx, rectCy, rectWidth, rectHeight, align = 'center', fill = 'cyan')
    # drawLabel('press space to begin', app.cx, rectCy, size = 30)

# def onMousePress(app, mouseX, mouseY):
    
# def onResiz

def main():
    runAppWithScreens(initialScreen='start')

main()