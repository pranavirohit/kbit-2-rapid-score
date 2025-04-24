'''
Button Class for UI Interactions

This file defines a simple Button class used in my KBIT-2 UI screens. 
Each button stores its position, dimensions, label (name), and an optional action 
function that gets called when the button is clicked.

The class handles basic hit detection based on mouse coordinates 
and delegates click behavior through the provided action function.

Class and method breakdown:

- __init__(name, left, top, width, height, action = None):
    Sets up a button with its display label, position, size, and an optional
    action function to trigger when the button is clicked.

- isClicked(mouseX, mouseY):
    Returns True if the mouse click falls within the button's rectangular area.

- handleClick(app):
    If the button has an assigned action, this calls it and passes in the app.

'''

from commonImports import *

class Button:
    def __init__(self, name, left, top, width, height, action = None):
        self.name = name
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.action = action

    def isClicked(self, mouseX, mouseY):
        minX = self.left
        maxX = self.left + self.width
        minY = self.top
        maxY = self.top + self.height

        return ((minX <= mouseX <= maxX) and 
                (minY <= mouseY <= maxY))
    
    def handleClick(self, app):
        if self.action:
            self.action(app)