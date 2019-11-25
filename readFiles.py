# 2019-2020 Fundamentos de Programação
# Grupo N
# número nome
# número nome




def readDronesFile(fileName):
    """
    Converts a given file listing drones into a collection.

    Requires: fileName is str, the name of a .txt file listing drones,
    following the format specified in the project sheet.
    Ensures: list whose first element is ... <to complete>
    """
    outputList = []

    outputList.append(readHeader(fileName))

    fileIn = open(fileName, 'r')

    # ... <to complete>

    return outputList



def readHeader(fileName):

    # ... <to complete>

    fileIn.readline()
    time = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    day = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    company = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    scope = fileIn.readline().strip().replace("\n", "")

    return (day, time, company, scope)



