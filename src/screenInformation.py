from commonImports import *

def onAppStart(app):
    app.screenNames = ['start', 'info', 'template', 'upload', 'output1',
               'output2', 'output3', 'result', 'end' ]
    app.width, app.height = 960, 540
    app.cx, app.cy = app.width // 2, app.height // 2
    app.buttonCenters = []

def info_redrawAll(app):
    image = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\KBIT_2_Screen_2_Info.png"
    drawImage(image, app.cx, app.cy, align = 'center')

def info_onKeyPress(app, key):
    switchScreens(app, key, 'info')

def template_redrawAll(app):
    image = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\KBIT_2_Screen_3_Template.png"
    drawImage(image, app.cx, app.cy, align = 'center')

def template_onKeyPress(app, key):
    switchScreens(app, key, 'template')

def upload_redrawAll(app):
    image = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\KBIT_2_Screen_4_File_Info.png"
    drawImage(image, app.cx, app.cy, align = 'center')

def upload_onKeyPress(app, key):
    switchScreens(app, key, 'upload')

def output1_redrawAll(app):
    image = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\KBIT_2_Screen_5_Output_Data_1.png"
    drawImage(image, app.cx, app.cy, align = 'center')

def output1_onKeyPress(app, key):
    switchScreens(app, key, 'output1')

def output2_redrawAll(app):
    image = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\KBIT_2_Screen_6_Output_Data_2.png"
    drawImage(image, app.cx, app.cy, align = 'center')

def output2_onKeyPress(app, key):
    switchScreens(app, key, 'output2')

def output3_redrawAll(app):
    image = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\KBIT_2_Screen_7_Output_Data_3.png"
    drawImage(image, app.cx, app.cy, align = 'center')

def output3_onKeyPress(app, key):
    switchScreens(app, key, 'output3')

def result_redrawAll(app):
    image = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\KBIT_2_Screen_8_Results.png"
    drawImage(image, app.cx, app.cy, align = 'center')

def result_onKeyPress(app, key):
    switchScreens(app, key, 'result')

def end_redrawAll(app):
    image = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\KBIT_2_Screen_9_Thank_You.png"
    drawImage(image, app.cx, app.cy, align = 'center')

def end_onKeyPress(app, key):
    switchScreens(app, key, 'end')

def switchScreens(app, key, current):
    index = app.screenNames.index(current)
    finalIndex = len(app.screenNames) - 1
    if key == 'space' and index < finalIndex:
        setActiveScreen(app.screenNames[index + 1])
    if key == 'backspace' and index > 0:
        setActiveScreen(app.screenNames[index - 1])

def main():
    runAppWithScreens(initialScreen = 'start')

main()