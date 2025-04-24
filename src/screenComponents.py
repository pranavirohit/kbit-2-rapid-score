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