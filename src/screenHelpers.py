'''
UI Button + Screen Helpers

This file includes helper functions for working with buttons and switching screens 
in my KBIT-2 interface. It handles button creation, click detection, and logic 
for moving between different app screens (like start, input, results, etc.).

Here's what each function does:

- getButtonWidth(left, top, right, bottom):
    Returns the width of a button based on its bounding box.

- getButtonHeight(left, top, right, bottom):
    Returns the height of a button based on its bounding box.

- createButton(name, left, top, right, bottom, action):
    Creates a Button object using bounding box coordinates. Automatically calculates
    width and height before the button is initialized. I used this function because
    I relied on the pixel coordinates from the UI images I created when placing buttons.

- switchScreens(app, key, screen):
    Handles moving forward or backward through screens based on the key pressed.
    Calls both prevScreen and nextScreen to check for valid transitions.

- nextScreen(app, key, screen):
    If the current screen isn't the last one and the space key is pressed,
    moves to the next screen in app.screenNames.

- prevScreen(app, key, screen):
    If the current screen isn't the first one and the backspace key is pressed,
    moves to the previous screen in app.screenNames.

- getScreenIndex(app, screen):
    Helper function that returns the index of the current screen and 
    the index of the final screen in the screen list.

- clickButtons(app, screen, mouseX, mouseY):
    Checks all button objects on the current screen. If one is clicked, 
    it calls the button's handleClick method to trigger its action.
    → Recommended by ChatGPT: Use .values() shorthand instead of another loop
    to go through each button and check if it's clicked

'''

from commonImports import *
def getButtonWidth(left, top, right, bottom):
    return right - left

def getButtonHeight(left, top, right, bottom):
    return bottom - top

def createButton(name, left, top, right, bottom, action):
    width = getButtonWidth(left, top, right, bottom)
    height = getButtonHeight(left, top, right, bottom)
    return Button(name, left, top, width, height, action)

def switchScreens(app, key, screen):
    prevScreen(app, key, screen)
    nextScreen(app, key, screen)

def nextScreen(app, key, screen):
    index, finalIndex = getScreenIndex(app, screen)
    if key == 'space' and index < finalIndex:
        setActiveScreen(app.screenNames[index + 1])

def prevScreen(app, key, screen):
    index, finalIndex = getScreenIndex(app, screen)
    if key == 'backspace' and index > 0:
        setActiveScreen(app.screenNames[index - 1])

def getScreenIndex(app, screen):
    index = app.screenNames.index(screen)
    finalIndex = len(app.screenNames) - 1
    return index, finalIndex

def clickButtons(app, screen, mouseX, mouseY):
    if screen in app.buttonsByScreen:
        # Added .values() shorthand instead of another loop (recommended by ChatGPT)
        for button in app.buttonsByScreen[screen].values():
            if button.isClicked(mouseX, mouseY):
                button.handleClick(app)