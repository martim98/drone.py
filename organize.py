import readFiles as rf
import constants as ct
#import writeFiles as wf
from copy import deepcopy
import timeD

def organizeDrones(fileName):
    """
    Function that reorganizes list of lists of drones

    Requires: A list of lists with the drone information retrieved
    from the readFiles.py function "readDronesFile()"
    Ensures: A list sorted in the same order of the list of lists
    of the parcels information
    """
    a = rf.readListing(fileName)
    while [''] in a: # remove [''] that were causing errors
        a.remove([''])
    orgOutListD = []
    for b in range(len(a)):
        dronesOgranized = []
        for i in range(0, 2):                   #1name, 2zone
            dronesOgranized.append(a[b][i].lstrip())
        for i in range(6, 8):                   #6 date, 7 time
            dronesOgranized.append(a[b][i].lstrip())
        dronesOgranized.append(a[b][3].lstrip())         #distance
        dronesOgranized.append(a[b][2].lstrip())         #weight
        dronesOgranized.append(a[b][5].lstrip())         #autonomy
        dronesOgranized.append(a[b][4].lstrip())         #cumulated distance
        orgOutListD.append(dronesOgranized)
    while [''] in orgOutListD: # this code is just to be sure that there are no [''] in the output list
        orgOutListD.remove([''])
    #print(orgOutListD)
    return ct.convertStrDrones(orgOutListD)

def organizeParcels(fileName):
    """Function to organize and prepare list of lists of parcels
    requires: the fileName of parcels
    ensures: A list of list with values adopted for further functions
    """
    a = rf.readListing(fileName)
    while [''] in a:
        a.remove([''])
    return ct.convertStrParcles(a)

#orgP = organizeParcels('parcels16h00_2019y11m5.txt')

def sortDrones(fileName):
    """Function that sorts list of drones
    Requires: A list of drones with their properties
    Ensures: A sorted list of drones
    """
    droneList = organizeDrones(fileName)
    droneList.sort(key = lambda x: (x[2], x[3], -x[6], x[0]))
    return droneList
    
def sortParcels(fileName):
    """Function that sorts list of parcels
    Requires: A list of parcels with their properties
    Ensures: A sorted list of parcels
    """
    parcelsList = organizeParcels(fileName)
    parcelsList.sort(key = lambda x: (x[2], x[3], x[5], x[0]))
    return parcelsList

#Psorted = sortParcels('parcels16h00_2019y11m5.txt')
#Dsorted = sortDrones('drones16h00_2019y11m5.txt')

def sortTimetable(timetable):
    """
    Function that sorts the output timetable in an
    expectd order and puts first the cancelled orders
        Order: first place the cancelled orders in 
    time-ascending order, then by name; then place matched
    orders by date, time, name
    
    Requires: a list of lists of matched orders
    Ensures: a sorted list of lists of matched orders
    """
    timetable.sort(key = lambda x: (x[0], x[1], x[2]))
    counter = 0
    for i in range(len(timetable)):
        if 'cancelled' in timetable[i][3]:
            timetable.insert(0, timetable.pop(i))
            counter += 1
    csort = sorted(timetable[0:counter], key = lambda x: (x[1], x[2]))
    csort.extend(timetable[counter:])
    return csort

#listD, writeTB = match('parcels16h00_2019y11m5.txt', 'drones16h00_2019y11m5.txt')

#s[0:6].sort(key = lambda x: (x[1], x[2]))
#test = sorted(s[0:5], key = lambda x: (x[1], x[2]))



def updateDrones(listDrones, listParcels, a, b):
    """
    Function that updates list of lists of drones

    Requires: A list with technical information retrieved from matching
    parcels and drones
    Ensures: an updated list of lists of each drone if needed
    """
    listDrones[b][6] -= ((listParcels[a][4]/1000)*2) # update the range
    listDrones[b][7] += (listParcels[a][4]/1000) * 2 # update the acumulated distance
    listDrones[b][2:4] = timeD.addTimeAsString(listDrones[b][2:4], listParcels[a][6])[0] # update/add the time
    #listDrones[b][2:4] = timeD.checkTime(listDrones[b][2:4], listParcels[a][6])
#    if timeD.giveDateTime(listDrones[b][2], listDrones[b][3]) > timeD.convertTime([listParcels[2], listParcels[3]]):
#        listDrones[b][2:4] = timeD.returnNewDate(listParcels[2:4])
#        listDrones[b][2:4] = timeD.addTimeAsString(listDrones[b][2:4], listParcels[a][6])[0]
    
    # return drones by sorting as specified in the project
    return listDrones.sort(key = lambda listDrones: (listDrones[2], listDrones[3], -listDrones[6], listDrones[7], listDrones[0]))




def match(fileName1, fileName2):
    """The core function, it matches drones with parcels
    Requires: two fileNames of parcels and drones in this order
    Ensures: A list of list of the drones matched with drones
    """
    #CHECK IF THE INPUT IS PARCELS AND DRONES (just titles)
    listD = sortDrones(fileName2)
    listP = sortParcels(fileName1)
    writeTB = []
    for a in range(len(listP)):
        h = True
        b = 0
        #for b in range(len(listD)):
        while h:
        #date:
            if (listP[a][2] == listD[b][2]) and listP[a][1] == listD[b][1] \
            and listP[a][4] <= listD[b][4] and listP[a][4] < listD[b][6]*1000 \
            and listP[a][5] <= listD[b][5]:
                #hour: if listP[a][3] >= listD[b][3]:
                #zone and distance and autonomy:
                #weight:
                maksimum = max(listD[b][3], listP[a][3])
                listD[b][3] = maksimum
                time = [listD[b][2], maksimum]


                if timeD.addTimeAsString(time, listP[a][6])[1] <= timeD.convertTime(time):
                    writeTB.append([listP[a][2], maksimum, listP[a][0], listD[b][0]])

                else:
                    writeTB.append(timeD.returnNewDate(time) + [listP[a][0], listD[b][0]])
                    listD[b][2:4] = timeD.returnNewDate(time)
                h = False
                updateDrones(listD, listP, a, b)
                
            else:
                if b == len(listD)-1:
                    writeTB.append([listP[a][2], listP[a][3], listP[a][0], "cancelled"])
                    h = False
            b +=1
#    for a in range(len(listP)):
#        h = True
#        b = 0
#        while h:
            
    writeTBsorted = sortTimetable(writeTB)
    print('this is the parcel list:', '\n', listP)
    print()
    print('this is the drones list:', '\n', listD)
    print()
    #print('this is the list of booleans that validated the conditions:', '\n', listF)
    #print()
    print('this would be the output list to the writeFiles', '\n', writeTBsorted)
    print(listD)
    return listD, writeTBsorted


d, s = match('parcels08h00_2019y12m14.txt', 'drones08h00_2019y12m14.txt')
#listDrUp, matched = match('parcels16h00_2019y11m5.txt', 'drones16h00_2019y11m5.txt')
#name = "parcels11h00_2019y11m5.txt"




