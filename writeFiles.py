import constants as ct
import timeD as td
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
    listDrUp, matched = org.match(fileName1, fileName2)
    #time = timeD.addTimeAsString(fileName1[2:4], fileName1[6])
    timeH, timeM = ct.takeTime(fileName1[7:12])
    dateY, dateM, dateD = ct.takeDate(fileName1[13:fileName1.find('.')])
    title = "timetable{:02d}h{:02d}_{}y{}m{}.txt".format(timeH, timeM, dateY, dateM, dateD)
    updatedFile = open(title, 'w')
    headerP = rf.getHeader(fileName1)
    headerP[-1] = "Timeline: \n"
    content = headerP
    matchedStr = listToString(matched)
    content.extend(matchedStr)
    #print(content)
    updatedFile.writelines(content)
    updatedFile.close()
    



writeTimetable('parcels11h00_2019y11m5.txt', 'drones11h00_2019y11m5.txt')
#writeDrones:
    #!add the 30 mins in the title

#REORGANIZE DRONES BEFORE! prepare.py

def reOrganizeDrones(list1):
    """
    Function that reverses the organizeDrones function

    Requires: The drone list of lists already updated
    Ensures: A list of lists of the drones prepared for the writing function
    """
    listDronesOrganizedF = []
    for b in range(len(list1)):
        auxList = []
        for i in range(0,2):
            auxList.append(list1[b][i])
        for i in range(-3, -5, -1):
            auxList.append(int(list1[b][i]))
        for i in range(-1, -3, -1):
            auxList.append(round(list1[b][i], 1))
        for i in range(2,4):
            auxList.append(list1[b][i])
        listDronesOrganizedF.append(auxList)
    return listDronesOrganizedF
    #a function to reorganize the drones and also to turn round the floats


def writeDrones(fileName1, fileName2):
    """ Function that creates updated listing of drones for the following
    delivery schedule
    
    Requires: A list with technical information retrieved from matching
    parcels and drones
    Ensures: List of drones with updated availability time, autonomy and
    accumulated distance
    """
    listDrUp, matched = org.match(fileName1, fileName2)
    timeH1, timeM1 = ct.takeTime(fileName1[7:12])
    timeH1str = '{:02d}:{:02d}'.format(timeH1, timeM1)
    dateY, dateM, dateD = ct.takeDate(fileName1[13:fileName1.find('.')])
    timeDstr = '{}-{}-{}'.format(dateY, dateM, dateD)
    DTformat = td.addTimeAsString([timeDstr, timeH1str], 30)[0] #changes the format
    #to datatime AND add 30 mins AND output as a list of strings again
    timeH2, timeM2 = ct.takeTime(str(DTformat[1]))
    title = "drones{:02d}h{:02d}_{}y{}m{}.txt".format(timeH2, timeM2, dateY, dateM, dateD)
    # ALSO CHECK IF THE DAY ENDS??
    updatedFile = open(title, 'w')
    headerD = rf.getHeader(fileName2)
    headerD[1] = '{:02d}h{:02d}\n'.format(timeH2, timeM2) #changing the time in the header
    content = headerD
    listDrStr = listToString(reOrganizeDrones(listDrUp))
    content.extend(listDrStr)
    print(content)
    updatedFile.writelines(content)
    updatedFile.close()


writeDrones('parcels11h00_2019y11m5.txt', 'drones11h00_2019y11m5.txt')



            

#from organize import match
#listDr, matched = match('parcels16h00_2019y11m5.txt', 'drones16h00_2019y11m5.txt')

#Listing = listToString(matched)
