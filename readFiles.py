# 2019-2020 Fundamentos de Programação
# Grupo N
# número nome
# número nome


def readHeader(fileName):
    #Status - Working
    """
    Reads the header of the text file and return as a tuple

    requires: a text file, either drone input file or parcels input
    ensures: a tuple with the day, time, company and scope present in the header
    """
    outputListH = []
    fileInH = open(fileName, 'r')
    content = fileInH.readlines()
    for line in content:
        outputListH.append(line.replace('\n', ''))
    fileInH.close()
    return tuple(outputListH[:6])


def readDronesFile(fileName):
    #status - Working
    """
    Converts a given file listing drones into a collection.

    Requires: fileName is str, the name of a .txt file listing drones,
    following the format specified in the project sheet.
    Ensures: list whose first element is ... <to complete>
    """
    outputListD = []
    fileIn1 = open(fileName, 'r')
    content = fileIn1.readlines()
    for line in content:
        outputListD.append(line.replace('\n', '').split(','))
    fileIn1.close()
    return outputListD[7:]




def readParcelsFile(fileName):
    #Status - Working
    """Converts a given file listing parcels into a collection.

       Requires: fileName is str, the name of a .txt file listing the parcels,
       following the format specified in the project sheet.
       Ensures: list whose first element is ... <to complete>
       """
    outputListP = []
    fileIn2 = open(fileName, 'r')
    content = fileIn2.readlines()
    for line in content:
        outputListP.append(line.replace('\n', '').split(','))
    fileIn2.close()
    return outputListP[7:]







