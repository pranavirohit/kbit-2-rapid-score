from commonImports import *

def start_redrawAll(app):
    image = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\KBIT_2_Start_Screen.png"
    drawImage(image, app.cx, app.cy, align = 'center')
    
def start_onKeyPress(app, key):
    switchScreens(app, key, 'start')