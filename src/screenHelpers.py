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
        # Added .values() shorthand instead of another loop 
        # (recommended by ChatGPT)
        for button in app.buttonsByScreen[screen].values():
            if button.isClicked(mouseX, mouseY):
                button.handleClick(app)