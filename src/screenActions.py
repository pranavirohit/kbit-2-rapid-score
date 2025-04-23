def downloadTemplateCSV(app):
    print("Downloading template CSV...")

def uploadTemplateCSV(app):
    print("Downloading template CSV...")

def downloadResultCSV(app):
    print("Downloading result CSV...")

def updateCSVCategories(app, testType):
    if testType == 'verbal':
        app.verbalSelected = True

def updateImages(app, screen):
    # app.nonverbalImage = 
    # app.iqImage = 

    if app.verbalSelected:
        # Rename file later
        app.verbalImage = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\6.png"
    else:
        app.verbalImage = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\KBIT_2_Screen_5_Output_Data_1.png"
    
    # if testType == 'nonverbal':
    #     app.nonverbalImage =