import operations as op
import timeD
import readFiles as rf
import organize as org

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
        newLine.strip(', ') #string
        newLine = newLine + '\n'
        newList.append(newLine)
    return newList


def writeTimetable(fileNameParcels, fileNameDrones):
    """
    Function that updates list of lists of drones

    Requires: file of parcels as fileNameParcels and file of drones as fileNameDrones
    Ensures: a txt output timetable.txt with respective date and hour of
    parcels matched with drones
    """
    rf.checkInternal(fileNameParcels, fileNameDrones)
    rf.checkTitles(fileNameParcels, fileNameDrones)
    listDrUp, matched = org.match(fileNameParcels, fileNameDrones)
    timeH, timeM = timeD.takeTime(fileNameParcels[7:12])
    dateY, dateM, dateD = timeD.takeDate(fileNameParcels[13:fileNameParcels.find('.')])
    title = "timetable{:02d}h{:02d}_{}y{}m{}.txt".format(timeH, timeM, dateY, dateM, dateD)
    updatedFile = open(title, 'w')
    headerP = rf.readHeader(fileNameParcels)
    headerP[-1] = "Timeline: \n"
    content = headerP
    matchedStr = listToString(matched)
    content.extend(matchedStr)
    updatedFile.writelines(content)
    updatedFile.close()


def reOrganizeDrones(list1):
    """
    Function that reverses the organizeDrones function

    Requires: The drone list of lists already updated
    Ensures: A list of lists of the drones prepared for the writing function
    """

    for b in range(len(list1)):
        for i in range(4, 6):
            list1[b][i] = round(list1[b][i], 1)
    return list1
    #a function to reorganize the drones and also to turn round the floats


def writeDrones(fileNameParcels, fileNameDrones):
    """
    Function that creates updated listing of drones for the following
    delivery schedule
    
    Requires: file of parcels as fileNameParcels and file of drones as fileNameDrones, in fixed order
    Ensures: List of drones with updated availability time, autonomy and
    accumulated distance
    """
    listDrUp, matched = org.match(fileNameParcels, fileNameDrones)
    timeH1, timeM1 = timeD.takeTime(fileNameParcels[7:12])
    timeH1str = '{:02d}:{:02d}'.format(timeH1, timeM1)
    dateY, dateM, dateD = timeD.takeDate(fileNameParcels[13:fileNameParcels.find('.')])
    timeDstr = '{}-{}-{}'.format(dateY, dateM, dateD)
    DTformat = timeD.addTime([timeDstr, timeH1str], 30)[0] #changes the format
    #to datatime AND add 30 mins AND output as a list of strings again
    timeH2, timeM2 = timeD.takeTime(str(DTformat[1]))
    title = "drones{:02d}h{:02d}_{}y{}m{}.txt".format(timeH2, timeM2, dateY, dateM, dateD)
    updatedFile = open(title, 'w')
    headerD = rf.readHeader(fileNameDrones)
    headerD[1] = '{:02d}h{:02d}\n'.format(timeH2, timeM2) #changing the time in the header
    content = headerD
    listDrStr = listToString(reOrganizeDrones(listDrUp))
    content.extend(listDrStr)
    updatedFile.writelines(content)
    updatedFile.close()


