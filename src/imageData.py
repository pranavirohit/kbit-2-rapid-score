from commonImports import *

testPage = r"C:\Users\pkroh\OneDrive - andrew.cmu.edu\2024-25\15-112\Term Project\data_files\page_78.png"
verbalTest, nonVerbalTest = splitImage(testPage)

verbalProcessed = processImage(verbalTest)
nonVerbalProcessed = processImage(nonVerbalTest)
print(extractAllText(verbalProcessed))
print(extractAllText(nonVerbalProcessed))

