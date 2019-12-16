# 2019-2020 Fundamentos de Programação
# Grupo N
# número nome
# número nome


def getHeader(fileName):
    """Fuction that receives the header from the drones or parcels file
    Requires: text file name
    Ensures: first 6 lines of the text file as a list of lines
    """
    fileIn = open(fileName, 'r')
    lines = fileIn.readlines()
    fileIn.close()
    
    return lines[:7]
#
#header = getHeader('drones11h00_2019y11m5.txt')
#tit = 'drones11h00_2019y11m5.txt'
#titType =   tit[0:tit.find('h')-2]
#titTime = tit[tit.find('h')-2:tit.find('_')]
#titDate = cst.takeDate(tit[tit.find('_')+1:tit.find('.')])
#titDlist = [titDate[2], titDate[1], titDate[0]]
#headDate = [int(x) for x in header[3].split('-')]
#titType == header[6].strip(':\n').lower()
#header[6]
#titTime == header[1].strip(':\n')
#header[1]
#titDlist == [int(x) for x in header[3].split('-')]

#CHECK THE TITLE AND THE HEADER - 

import constants as cst

def readListing(fileName):
    #status - Working
    """
    Converts a given file listing drones or parcels into a collection. Also
    checks if the file is internally compatible (if the info from title is equal
    to the info of the header).

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


def checkInternal(fileName1, fileName2):
    """
    
    """
    listFiles = [fileName1, fileName2]
    #listBool = []
    #outList = []
    for fileName in listFiles:
        titleType = fileName[0:fileName.find('h')-2]
        titleTime = fileName[fileName.find('h')-2:fileName.find('_')]
        titleDate = cst.takeDate(fileName[fileName.find('_')+1:fileName.find('.')])
        titleDateL = [titleDate[2], titleDate[1], titleDate[0]]
        header = getHeader(fileName)
        try:
            if not (titleType == header[6].strip(':\n').lower() and \
                titleTime == header[1].strip(':\n') and \
                titleDateL == [int(x) for x in header[3].split('-')]):    
                #listBool.append(True)
                #outList.append('')

                #listBool.append(False)
                #outList.append(fileName)
                    raise Exception
        except Exception:
            raise Exception("Name and header inconsistent in {} file!".format(fileName))
    #return [listBool, outList]

#raise ValueError("The input {} file is internally incompatible!".format(titleType))
#CHECK THE TITLES OF TWO FILES! (new function)--> to use in the allocate function

def checkTitles(fileName1, fileName2):
    """
    Checks if the titles of input files contain 'parcels' and 'drones' 
    and if the dates and hours are the same
    Requires: two file titles of a parcels file and a drone file
    fileName1 must be the parcels file
    fileName2 must be the drones file
    Ensures: returns boolean: True if the conditions are met and 
    False if the are not
    """
    strDateP = fileName1[fileName1.find('_')+1:fileName1.find('.')]
    strDateD = fileName2[fileName2.find('_')+1:fileName2.find('.')]
    strTimeP = fileName1[7:12] #ParcelsTime
    strTimeD = fileName2[6:11] #DronesTime
    try:
        if strTimeP == strTimeD and strDateP == strDateD:
            if fileName1[0:7] == 'parcels' and fileName2[0:6] == 'drones':
                return True
        else:
            raise Exception
    except Exception:
        #print(Exc)
        raise Exception("Input error: Inconsistent files {} and {}!".format(fileName1, fileName2))
        #return False

#checkTitles('parcels11h00_2019y11m5.txt', 'drones11h00_2019y11m5.txt')
#fileName1 = 'parcels11h00_2019y11m5.txt'
#fileName2 = 'drones11h00_2019y11m5.txt'
#strDateP = fileName1[fileName1.find('_')+1:fileName1.find('.')]
#strDateD = fileName2[fileName2.find('_')+1:fileName2.find('.')]
#strTimeP = fileName1[7:12] #ParcelsTime
#strTimeD = fileName2[6:11] #DronesTime
#strParcels = fileName1[0:7] 
#strDrones = fileName2[0:6]
