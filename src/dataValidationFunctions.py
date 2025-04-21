'''
For use with checking CSV file data
'''
# Come back to checking logic for isValidLine check, use these rules once
# you have CSV file

# def isValidLine(line, startingVal, endingVal):
#     rawScores = {'verbal1': [108, 52], 
#                  'verbal2': [51, 0],
#                  'nonverbal': [46, 0]}
    
#     line = line.strip
#     parts = line.split()
#     if len(parts) is 4:
#         rawScore = int(parts[0])
#         standScore = int(parts[1])
#         confInt = parts[2]
#         percentile = int(parts[3])

#         if ((rawScore > startingVal) or
#             (rawScore < endingVal)):
#             return False
        
#         if int(standScore) > 160:
#             return False

#         if percentile.startswith('>'):
#             check = percentile[1:]
#             if check > 99.9:
#                 return False

# def getPercentileNum(percentile):