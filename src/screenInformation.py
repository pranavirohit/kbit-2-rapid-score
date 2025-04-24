from commonImports import *
'''
KBIT-2 App Screens and UI Routing

This file defines the main screen flow and UI interactions for the KBIT-2 scoring 
interface. It sets up the list of screens used in the app, initializes app-wide 
variables (like which categories are selected or whether a file has been uploaded), 
and maps each screen to its background image and clickable button regions. 

Function breakdown:

- onAppStart(app):
    Initializes the app's screen size, button states, and screen order.
    Defines all buttons for each screen using pixel coordinates pulled 
    from UI mockups.
    → CMU Graphics Demos, Screens: https://drive.google.com/file/d/1VYohB0BBTMDXkcSet0ybSIXWYztXXonp/view
    → Recommended by ChatGPT: Use lambda function to delay screen change
    until button is clicked. Prior to this, when I tested the screens, 
    the screens would appear as if the buttons were already clicked, even 
    if I hadn't yet.

- [screen]_redrawAll(app):
    Loads and displays the background image for a given screen. If the
    screen is an output screen, where the user can select which categories
    they want to use in their result CSV, it uses 
    getOutputImage(app, screen) to load the correct image file path.
    → CMU Graphics Demos, Screens: https://drive.google.com/file/d/1VYohB0BBTMDXkcSet0ybSIXWYztXXonp/view

- [screen]_onKeyPress(app, key):
    Handles navigation between screens. Uses switchScreens to move 
    forward or backward depending on the key pressed. 
    → CMU Graphics Demos, Screens: https://drive.google.com/file/d/1VYohB0BBTMDXkcSet0ybSIXWYztXXonp/view

- [screen]_onMousePress(app, mouseX, mouseY):
    Checks if any buttons were clicked on the screen and calls their 
    associated action using clickButtons.
    → Recommended by ChatGPT: Use a single function to do this for all screens.
    Originally, I had used the same code/logic for each individual onMousePress,
    which I changed to a global function after asking for feedback on the 
    structure of my code. 

These functions exist for all screens in the flow:
'start', 'info', 'template', 'upload', 'output1', 'output2', 'output3', 
'result', and 'end'.

'''
def onAppStart(app):
    app.screenNames = [
        'start', 'info', 'template', 'upload', 'output1',
        'output2', 'output3', 'result', 'end'
    ]
    app.width, app.height = 960, 540
    app.cx, app.cy = app.width // 2, app.height // 2

    app.verbalSelected = False
    app.nonverbalSelected = False
    app.iqSelected = False
    app.fileUploaded = False

    # Added use of lambda function to delay screen change until button was clicked
    # Retrieved clickable areas by uploading images to a pixel selector tool

    app.buttonsByScreen = {
        'template': {
            'downloadBtn': createButton(
                'downloadBtn', 331, 415, 629, 464,
                action = downloadTemplateCSV
            )
        },
        'upload': {
            'uploadBtn': createButton(
                'uploadBtn', 343, 415, 616, 464,
                action = uploadTemplateCSV
            )
        },
        'output1': {
            'verbalSelectAll': createButton(
                'verbalBtn', 93, 252, 866, 322,
                action = lambda app=app: updateCSVCategories(app, 'verbal')
            )
        },
        'output2': {
            'nonverbalSelectAll': createButton(
                'nonverbalBtn', 93, 252, 866, 322,
                action = lambda app=app: updateCSVCategories(app, 'nonverbal')
            )
        },
        'output3': {
            'IQSelectAll': createButton(
                'IQBtn', 93, 252, 866, 322,
                action = lambda app=app: updateCSVCategories(app, 'iq')
            )
        },
        'result': {
            'downloadBtn': Button(
                'downloadBtn', 327, 416, 300, 50,
                action = downloadResultCSV
            )
        },
        'end': {
            'homepageBtn': createButton(
                'homepageBtn', 330, 310, 628, 358,
                action = loadHomescreen
            )
        }
    }

def start_redrawAll(app):
    image = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project"
        r"\user_experience\KBIT_2_Start_Screen.png"
    )
    drawImage(image, app.cx, app.cy, align = 'center')

def start_onKeyPress(app, key):
    switchScreens(app, key, 'start')

def info_redrawAll(app):
    image = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project"
        r"\user_experience\KBIT_2_Screen_2_Info.png"
    )
    drawImage(image, app.cx, app.cy, align = 'center')

def info_onKeyPress(app, key):
    switchScreens(app, key, 'info')

def template_redrawAll(app):
    image = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project"
        r"\user_experience\KBIT_2_Screen_3_Template.png"
    )
    drawImage(image, app.cx, app.cy, align = 'center')

def template_onKeyPress(app, key):
    switchScreens(app, key, 'template')

def template_onMousePress(app, mouseX, mouseY):
    clickButtons(app, 'template', mouseX, mouseY)

def upload_redrawAll(app):
    image = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project"
        r"\user_experience\KBIT_2_Screen_4_File_Info.png"
    )
    drawImage(image, app.cx, app.cy, align = 'center')

def upload_onKeyPress(app, key):
    if app.fileUploaded:
        nextScreen(app, key, 'upload')
    else:
        prevScreen(app, key, 'upload')

def upload_onMousePress(app, mouseX, mouseY):
    clickButtons(app, 'upload', mouseX, mouseY)

def output1_redrawAll(app):
    image = getOutputImage(app, 'output1')
    drawImage(image, app.cx, app.cy, align = 'center')

def output1_onKeyPress(app, key):
    switchScreens(app, key, 'output1')

def output1_onMousePress(app, mouseX, mouseY):
    clickButtons(app, 'output1', mouseX, mouseY)

def output2_redrawAll(app):
    image = getOutputImage(app, 'output2')
    drawImage(image, app.cx, app.cy, align = 'center')

def output2_onKeyPress(app, key):
    switchScreens(app, key, 'output2')

def output2_onMousePress(app, mouseX, mouseY):
    clickButtons(app, 'output2', mouseX, mouseY)

def output3_redrawAll(app):
    image = getOutputImage(app, 'output3')
    drawImage(image, app.cx, app.cy, align = 'center')

def output3_onKeyPress(app, key):
    switchScreens(app, key, 'output3')

def output3_onMousePress(app, mouseX, mouseY):
    clickButtons(app, 'output3', mouseX, mouseY)

def result_redrawAll(app):
    image = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project"
        r"\user_experience\KBIT_2_Screen_8_Results.png"
    )
    drawImage(image, app.cx, app.cy, align = 'center')

def result_onKeyPress(app, key):
    switchScreens(app, key, 'result')

def result_onMousePress(app, mouseX, mouseY):
    clickButtons(app, 'result', mouseX, mouseY)

def end_redrawAll(app):
    image = (
        r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project"
        r"\user_experience\KBIT_2_Screen_9_Thank_You.png"
    )
    drawImage(image, app.cx, app.cy, align = 'center')

def end_onKeyPress(app, key):
    switchScreens(app, key, 'end')

def end_onMousePress(app, mouseX, mouseY):
    clickButtons(app, 'end', mouseX, mouseY)

def main():
    runAppWithScreens(initialScreen = 'start')

main()
