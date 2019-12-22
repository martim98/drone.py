# 2019-2020 Fundamentos de Programacao
# Grupo 30
# 54070 Kinga Bondyra
# 55066 Martim Almeida

import timeD
import constants as ct


def readHeader(fileName):
    """
    Fuction that receives the header from the drones or parcels file

    Requires: text file name
    Ensures: first 6 lines of the text file as a list of lines
    """
    fileIn = open(fileName, 'r')
    lines = fileIn.readlines()
    fileIn.close()

    return lines[:7]


def readListing(fileName):
    """
    Converts a given file listing drones or parcels into a list of lists.

    Requires: the name of a listing drones file in .txt,
    following the format specified in the project sheet
    Ensures: list of lists of strings with the drones specification or
    parcels information
    """
    outputList = []
    fileIn = open(fileName, 'r')
    content = fileIn.readlines()
    for line in content:
        outputList.append(line.replace('\n', '').split(','))
    fileIn.close()

    return outputList[7:]


def checkInternal(fileName):
    """ Function that check if fileName title is consistent
    with the header

    Requires: name of the drones or parcels file
    Ensures: raises an asserion error if the filename is not consistent
    with the header, returns nothing if the file is consistent
    """

    titleType = fileName[0:fileName.find('h')-2]
    titleTime = fileName[fileName.find('h')-2:fileName.find('_')]
    titleDate = timeD.takeDate(fileName[fileName.find('_')+1:fileName.find('.')])
    titleDateL = [titleDate[2], titleDate[1], titleDate[0]]
    header = readHeader(fileName)

    assert (titleType == header[ct.H_SCOPE].strip(':\n').lower() and
            titleTime == header[ct.H_TIME].strip(':\n') and
            titleDateL == [int(x) for x in header[ct.H_DAY].split('-')]), \
            "Input Error: Name and header inconsistent in {} file!".format(fileName)
        


def checkTitles(fileNameParcels, fileNameDrones):
    """
    Checks if the titles of input files contain 'parcels' and 'drones' 
    and if the dates and hours are the same

    Requires: two file titles:
    fileNameParcels must be the parcels file
    fileNameDrones must be the drones file
    Ensures: raises an assertion error if the files are inconsistent,
    returns nothing if the files are correct
    """
    strDateP = fileNameParcels[fileNameParcels.find('_')+1:fileNameParcels.find('.')]
    strDateD = fileNameDrones[fileNameDrones.find('_')+1:fileNameDrones.find('.')]
    strTimeP = fileNameParcels[7:12]
    strTimeD = fileNameDrones[6:11]

    assert (strTimeP == strTimeD and strDateP == strDateD and
    fileNameParcels[0:7] == ct.P_TITLE and fileNameDrones[0:6] == ct.D_TITLE), \
    "Input error: Inconsistent files {} and {}!".format(fileNameParcels, fileNameDrones)

