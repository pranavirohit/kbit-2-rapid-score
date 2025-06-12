import cv2 # OpenCV
import os
import pytesseract as pyt # Tesseract
import pandas as pd
import re
import tkinter.filedialog
import shutil

from PIL import Image as PILImage
from cmu_graphics import* # CMU graphics
from pdf2image import convert_from_path #PDF2Image

from imageProcessingFunctions import (
    processPDF,
    splitImage,
    processImage,
    getTableAge,
    getVerticalLinesPositions,
    thresholdImage,
    isolateVerticalLines,
    splitThreeTables,
    findMidpoint
)

from dataExtractionFunctions import (
    extractAllText,
    cleanTextToList,
    checkDecimalPoints,
    isValidLength,
    getNumericalValues,
    rawScoreValues,
    createDataFrame,
    listToDataFrame,
    dataFrameToCSV
)

from screenComponents import (
    Button
)

from screenActions import (
    downloadTemplateCSV,
    uploadTemplateCSV,
    downloadResultCSV,
    updateCSVCategories,
    getOutputImage,
    loadHomescreen
)
from screenHelpers import (
    getButtonWidth,
    getButtonHeight,
    createButton,
    switchScreens,
    prevScreen,
    nextScreen,
    getScreenIndex,
    clickButtons
)

# Order of import statements matter, must add dataRetrieval.py functions prior 
# to calling ANY dataProcessing.py functions

from dataRetrieval import (
    readTableB1CSV,
    separateInterval,
    descriptiveCategory,
    significanceLevel,
)

def test(func):
    def wrapper():
        try:
            func()
            print(f'[✓] {func.__name__} passed!')
        except AssertionError as e:
            print(f'[✗] {func.__name__} failed: {e}')
    return wrapper

from dataProcessing import (
    processUploadedFile, 
    createFileDict,
    buildParticipantResults
)