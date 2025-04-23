from commonImports import *

def onAppStart(app):
    app.screenNames = ['start', 'info', 'template', 'upload', 'output1',
               'output2', 'output3', 'results', 'end' ]
    app.width, app.height = 960, 540
    app.cx, app.cy = app.width // 2, app.height // 2
    app.buttonCenters = []

def start_redrawAll(app):
    image = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\KBIT_2_Start_Screen.png"
    drawImage(image, app.cx, app.cy, align = 'center')
    
def start_onKeyPress(app, key):
    switchScreens(app, key, 'start')

def info_redrawAll(app):
    image = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\KBIT_2_Screen_2_Info.png"
    drawImage(image, app.cx, app.cy, align = 'center')

def info_onKeyPress(app, key):
    switchScreens(app, key, 'info')

def template_redrawAll(app):
    image = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\KBIT_2_Screen_3_Template.png"
    drawImage(image, app.cx, app.cy, align = 'center')

def switchScreens(app, key, current):
    index = app.screenNames.index(current)
    finalIndex = len(app.screenNames) - 1
    if key == 'space' and index < finalIndex:
        setActiveScreen(app.screenNames[index + 1])
    if key == 'backspace' and index < 0:
        setActiveScreen(app.screenNames[index - 1])

def main():
    runAppWithScreens(initialScreen = 'start')

main()