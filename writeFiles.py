import operations as op
import timeD
import readFiles as rf
import organize as org

#CHECK FOR THE COMMA ON THE END OF THE LINE
#CHECK writeDrones AFTER UPDATING!
#- done for Timetable: SORTING ACCORDING OT THE PDF REQUIREMENTS

def listToString(listOfLists):
    """Function that converts list of lists of strings to a list of strings
    Requires: list of lists of strings
    Ensures: list of strings
    """
    newList = list()
    for x in listOfLists:
        newLine = ''
        for y in x:
            newLine = newLine+str(y)+', '  #string
        newLine = newLine+'\n'
        newList.append(newLine.rstrip(', '))
    return newList


def writeTimetable(fileName1, fileName2):
    """ Function that updates list of lists of drones
    !
    Requires: file of parcels as fileName1 and file of drones as fileName2
    ...
    Ensures: 
    """
    rf.checkInternal(fileName1, fileName2)
    rf.checkTitles(fileName1, fileName2)
    listDrUp, matched = org.match(fileName1, fileName2)
    timeH, timeM = timeD.takeTime(fileName1[7:12])
    dateY, dateM, dateD = timeD.takeDate(fileName1[13:fileName1.find('.')])
    title = "timetable{:02d}h{:02d}_{}y{}m{}.txt".format(timeH, timeM, dateY, dateM, dateD)
    updatedFile = open(title, 'w')
    headerP = rf.readHeader(fileName1)
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


def writeDrones(fileName1, fileName2):
    """
    Function that creates updated listing of drones for the following
    delivery schedule
    
    Requires: file of parcels as fileName1 and file of drones as fileName2, in fixed order
    Ensures: List of drones with updated availability time, autonomy and
    accumulated distance
    """
    listDrUp, matched = org.match(fileName1, fileName2)
    timeH1, timeM1 = timeD.takeTime(fileName1[7:12])
    timeH1str = '{:02d}:{:02d}'.format(timeH1, timeM1)
    dateY, dateM, dateD = timeD.takeDate(fileName1[13:fileName1.find('.')])
    timeDstr = '{}-{}-{}'.format(dateY, dateM, dateD)
    DTformat = timeD.addTimeAsString([timeDstr, timeH1str], 30)[0] #changes the format
    #to datatime AND add 30 mins AND output as a list of strings again
    timeH2, timeM2 = timeD.takeTime(str(DTformat[1]))
    title = "drones{:02d}h{:02d}_{}y{}m{}.txt".format(timeH2, timeM2, dateY, dateM, dateD)
    updatedFile = open(title, 'w')
    headerD = rf.readHeader(fileName2)
    headerD[1] = '{:02d}h{:02d}\n'.format(timeH2, timeM2) #changing the time in the header
    content = headerD
    listDrStr = listToString(reOrganizeDrones(listDrUp))
    content.extend(listDrStr)
    updatedFile.writelines(content)
    updatedFile.close()


