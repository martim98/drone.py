# 2019-2020 Fundamentos de Programação
# Grupo N
# número nome
# número nome




def readHeader(fileName):
    """Fuction that receives the header from the drones or parcels file
    Requires: text file name
    Ensures: first 6 lines of the text file as a list of lines
    """
    fileIn = open(fileName, 'r')
    lines = fileIn.readlines()
    fileIn.close()
    
    return lines[:7]


#CHECK THE TITLE AND THE HEADER - 
def readListing(fileName):
    #status - Working
    """
    Converts a given file listing drones or parcels into a collection.

    Requires: fileName is str, the name of a .txt file listing drones,
    following the format specified in the project sheet.
    Ensures: list whose first element is ... <to complete>
    """
    outputList = []
    fileIn = open(fileName, 'r')
    content = fileIn.readlines()
    for line in content:
        outputList.append(line.replace('\n', '').split(','))
    fileIn.close()
    return outputList[7:]


#CHECK THE TITLES OF TWO FILES! (new function)