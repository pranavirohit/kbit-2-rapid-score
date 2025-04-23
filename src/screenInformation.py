from commonImports import *

def onAppStart(app):
    app.screenNames = ['start', 'info', 'template', 'upload', 'output1',
               'output2', 'output3', 'result', 'end' ]
    app.width, app.height = 960, 540
    app.cx, app.cy = app.width // 2, app.height // 2
    app.verbalSelected, app.nonverbalSelected, app.iqSelected = False, False, False

    app.buttonsByScreen = {
        'template': {
            'downloadBtn': Button('downloadBtn', 327, 416, 300, 50, action = downloadTemplateCSV)
        },
        'upload': {
            'uploadBtn': Button('uploadBtn', 343, 415, 270, 50, action = uploadTemplateCSV)
        },
        'output1': {
            'verbalSelectAll': createButton('verbalBtn', 93, 252, 866, 322, action = updateCSVCategories(app, 'verbal'))
        }
        # 'output2': {
        #     'nonverbalSelectAll': createButton('nonverbalBtn', 93, 252, 866, 322)
        # },
        # 'output3': {
        #     'IQSelectAll': createButton('IQBtn', 93, 252, 866, 322, action = updateIQScreen)
        # },
        # 'result': {
        #     'downloadBtn': createButton(name, left, top, right, bottom, action)
        # }
    }

def getButtonWidth(left, top, right, bottom):
    return right - left

def getButtonHeight(left, top, right, bottom):
    return bottom - top

def createButton(name, left, top, right, bottom, action):
    width = getButtonWidth(left, top, right, bottom)
    height = getButtonHeight(left, top, right, bottom)
    return Button(name, left, top, width, height, action)

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
    
    button = app.buttonsByScreen['template']['downloadBtn']
    drawRect(button.left, button.top, button.width, button.height, fill = 'black')

def template_onKeyPress(app, key):
    switchScreens(app, key, 'template')

def template_onMousePress(app, mouseX, mouseY):
    clickButtons(app, 'template', mouseX, mouseY)

def upload_redrawAll(app):
    image = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\KBIT_2_Screen_4_File_Info.png"
    drawImage(image, app.cx, app.cy, align = 'center')

def upload_onKeyPress(app, key):
    switchScreens(app, key, 'upload')

def output1_redrawAll(app):
    if app.verbalSelected:
        image = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\6.png"
    else:
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

def switchScreens(app, key, screen):
    index = app.screenNames.index(screen)
    finalIndex = len(app.screenNames) - 1
    if key == 'space' and index < finalIndex:
        setActiveScreen(app.screenNames[index + 1])
    if key == 'backspace' and index > 0:
        setActiveScreen(app.screenNames[index - 1])

def clickButtons(app, screen, mouseX, mouseY):
    if screen in app.buttonsByScreen:
        # Added .values() shorthand instead of another loop (recommended by ChatGPT)
        for button in app.buttonsByScreen[screen].values():
            if button.isClicked(mouseX, mouseY):
                button.handleClick(app)

def main():
    runAppWithScreens(initialScreen = 'start')

main()