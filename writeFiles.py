import timeD
import readFiles as rf
import organize as org
import constants as ct

def listToString(listOfLists):
    """
    Function that converts list of lists of strings to a list of strings

    Requires: list of lists of strings
    Ensures: list of strings
    """
    newList = list()
    for x in listOfLists:
        newLine = ''
        for y in x:
            newLine = newLine + str(y) + ', '
        newLine = newLine.strip(', ') + '\n'
        newList.append(newLine)
    return newList


def writeTimetable(fileNameParcels, fileNameDrones):
    """
    Function that updates list of lists of drones

    Requires: file of parcels as fileNameParcels and file of drones as fileNameDrones
    Ensures: a txt output timetable.txt with respective date and hour of
    parcels matched with drones
    """
    #checking if files are compatible
    rf.checkInternal(fileNameParcels, fileNameDrones)
    rf.checkTitles(fileNameParcels, fileNameDrones)
    
    listDrUp, matched = org.match(fileNameParcels, fileNameDrones)
    
    #collecting hour and date information
    timeH, timeM = timeD.takeTime(fileNameParcels[7:12])
    dateY, dateM, dateD = timeD.takeDate(fileNameParcels[13:fileNameParcels.find('.')])
    
    #creating a new file
    title = 'timetable{:02d}h{:02d}_{}y{}m{}.txt'.format(timeH, timeM, dateY, dateM, dateD)
    updatedFile = open(title, 'w')
    headerP = rf.readHeader(fileNameParcels)
    
    #changing header's scope
    headerP[ct.H_SCOPE] = ct.T_SCOPE
    content = headerP
    matchedStr = listToString(matched)
    content.extend(matchedStr)
    updatedFile.writelines(content)
    updatedFile.close()


def reOrganizeDrones(list1):
    """
    Function that prepares drones list of lists for the output .txt

    Requires: The drone list of lists already updated
    Ensures: A list of lists of the drones prepared for the writing function
    """

    for b in range(len(list1)):
        for i in range(4, 6):
            list1[b][i] = round(list1[b][i], 1)
    return list1



def writeDrones(fileNameParcels, fileNameDrones):
    """
    Function that creates updated listing of drones for the following
    delivery schedule
    
    Requires: file of parcels as fileNameParcels and file of drones as fileNameDrones, in fixed order
    Ensures: List of drones with updated availability time, autonomy and
    accumulated distance
    """
    listDrUp, matched = org.match(fileNameParcels, fileNameDrones)
    
    #collecting hour information
    timeH1, timeM1 = timeD.takeTime(fileNameParcels[7:12])
    timeH1str = '{:02d}:{:02d}'.format(timeH1, timeM1)
    
    #collecting date information
    dateY, dateM, dateD = timeD.takeDate(fileNameParcels[13:fileNameParcels.find('.')])
    timeDrStr = '{}-{}-{}'.format(dateY, dateM, dateD)
    
    #changes the format to datatime AND add 30 mins AND output as a list of strings again
    DTformat = timeD.addTime([timeDrStr, timeH1str], ct.TIME_DELTA)[ct.AS_STRING]
    timeH2, timeM2 = timeD.takeTime(str(DTformat[1]))
    
    #creating a new file
    title = "drones{:02d}h{:02d}_{}y{}m{}.txt".format(timeH2, timeM2, dateY, dateM, dateD)
    updatedFile = open(title, 'w')
    headerD = rf.readHeader(fileNameDrones)
    
    #changing the time in the header
    headerD[ct.H_TIME] = '{:02d}h{:02d}\n'.format(timeH2, timeM2)
    
    content = headerD
    listDrStr = listToString(reOrganizeDrones(listDrUp))
    content.extend(listDrStr)
    updatedFile.writelines(content)
    updatedFile.close()


