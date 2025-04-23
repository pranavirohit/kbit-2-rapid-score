from commonImports import *

def downloadTemplateCSV(app): # Code from ChatGPT
    sourcePath = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\KBIT2_Rapid_Score_Data_Template.xlsx"
    
    destPath = tkinter.filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx")],
        title="Save KBIT-2 Template As..."
    )
    
    if destPath:
        shutil.copyfile(sourcePath, destPath)
        print(f"Template saved to: {destPath}")
    else:
        print("Download canceled.")

def uploadTemplateCSV(app): # Code from ChatGPT
    print("Opening file dialog for upload...")
    
    filePath = tkinter.filedialog.askopenfilename(
        title = "Select filled-in KBIT-2 template",
        filetypes = [("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("All files", "*.*")]
    )
    
    if filePath:
        app.uploadedPath = filePath
        app.fileUploaded = True
        print(f"Uploaded file: {app.uploadedPath}")
        # processUploadedFile(app, filePath)
        
    else:
        print("No file selected.")
    print("Uploading template CSV...")

def downloadResultCSV(app):
    print("Preparing result CSV for download...")

    resultPath = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\KBIT_Results_Final_Data.xlsx"
    
    if not os.path.exists(resultPath):
        print("Processed results file not found.")
        return

    savePath = tkinter.filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes = [("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("All files", "*.*")],
        title="Save Processed Results As..."
    )

    if savePath:
        try:
            shutil.copyfile(resultPath, savePath)
            print(f"Result CSV successfully saved to: {savePath}")
        except Exception as e:
            print(f"Error saving file: {e}")
    else:
        print("Save canceled.")

def updateCSVCategories(app, testType):
    if testType == 'verbal':
        app.verbalSelected = True
    elif testType == 'nonverbal':
        app.nonverbalSelected = True
    elif testType == 'iq':
        app.iqSelected = True
    
def getOutputImage(app, screen):
    if screen == 'output1':
        if app.verbalSelected:
            return r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\6.png"
        else:
            return r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\KBIT_2_Screen_5_Output_Data_1.png"
    
    elif screen == 'output2':
        if app.nonverbalSelected:
            return r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\7.png"
        else:
            return r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\KBIT_2_Screen_6_Output_Data_2.png"

    elif screen == 'output3':
        if app.iqSelected:
            return r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\8.png"
        else:
            return r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\user_experience\KBIT_2_Screen_7_Output_Data_3.png"

def loadHomescreen(app):
    setActiveScreen(app.screenNames[0])