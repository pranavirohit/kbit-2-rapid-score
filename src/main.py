'''
Please note: the UI and scoring logic will be built here after the data has
been extracted and cleaned. 

Please see the logbook.txt for my work in building out/defining an algorithm for data 
processing, as that was a significant part of my work.
 
Please also see this document for how I plan to create the scoring logic, mapping each value
to a cell in the table with the data (what I hope to produce through data extraction): 
https://ash-trawler-907.notion.site/K-BIT2-Scoring-1cd5c24faeb080ce9fe8d882825b6d2d?pvs=4


See these other files for more details:

- helperFunctions.py:
    Contains all core processing functions for splitting pages, thresholding,
    detecting vertical lines, and cropping tables from full-page images.

- commonImports.py:
    File with all shared imports (OpenCV, Tesseract, PIL, etc.), as I 
    ran into a problem with keeping track of the import statements I used
    across files as I updated them. 

- imageImport.py:
    Code to generate images for processing/save them to my folder. This
    code is quite brief because I wanted the bulk of the logic/complexity
    to be within the helper functions.

- debuggingFunctions.py:
    Tool for inspecting intermediate outputs like line positions. 
    Used mostly for testing and verifying steps manually.

- logbook.txt:
    Notes on how I developed each part of the pipeline — includes thoughts,
    failed attempts, and explanations of key decisions. 

The goal is to build a user-friendly tool, but that depends on first extracting
the full dataset cleanly from the scanned pages.
'''
