import readFiles as rf
import operations as op
import timeD
import prepare as pr
from copy import deepcopy


def organizeDrones(fileName):
    """
    Function that reorganizes list of lists of drones

    Requires: A list of lists with the drone information retrieved
    from the readFiles.py function "readDronesFile()"
    Ensures: A list sorted in the same order of the list of lists
    of the parcels information
    """
    a = rf.readDronesFile(fileName)
    while [''] in a: # remove [''] that were causing errors
        a.remove([''])
    orgOutListD = []
    for b in range(len(a)):
        dronesOgranized = []
        for i in range(0, 2):
            dronesOgranized.append(a[b][i])
        for i in range(6, 8):
            dronesOgranized.append(a[b][i])
        dronesOgranized.append(a[b][3])
        dronesOgranized.append(a[b][2])
        dronesOgranized.append(a[b][5])
        dronesOgranized.append(a[b][4])
        orgOutListD.append(dronesOgranized)
    while [''] in orgOutListD: # this code is just to be sure that there are no [''] in the output list
        orgOutListD.remove([''])

    return op.convertStrDrones(orgOutListD)

def organizeParcels(fileName):
    """
    Function to organize and prepare list of lists of parcels

    requires: the fileName of parcels
    ensures: A list of list with values adpted for further functions
    """
    parcelsOrganized = rf.readParcelsFile(fileName)
    while [''] in parcelsOrganized:
        parcelsOrganized.remove([''])
    return op.convertStrParcles(parcelsOrganized)

def match(fileName1, fileName2):
    """
    The core function, it matches drones with parcels

    Requires: two fileNames of parcels and drones in this order
    Ensures: A list of list of the drones matched with drones
    """
    listParcels = organizeParcels(fileName1)
    listDrones = organizeDrones(fileName2)
    listF =[]
    writeTB = []
    writeFinal = []
    bole1 = True
    a = 0 #this should be 0
    counter = 0
    counter2 = 0
    while bole1: # this is the loop for the parcels
        bole2 = True
        b = 0
        counter1 = counter
        while bole2: # this is the loop for the drones
            listBool = []
            for i in range(1, 3):
                listBool.append(listParcels[a][i] == listDrones[b][i]) # checking the zone and the date
            for i in range(4, 6):
                listBool.append(listDrones[b][i] >= listParcels[a][i]) # checking the max distance and the weight
            listBool.append(listDrones[b][6]*1000 > listParcels[a][4]) # checking if has enough range
            listF.append(listBool)

            # checking the booleans and matching
            if False not in listBool:
                # the first if checking the order time is bigger than the drone's
                if timeD.giveDateTime(listDrones[b][2], listDrones[b][3]) <= timeD.giveDateTime(listParcels[a][2], listParcels[a][3]):
                    writeTB.append([listParcels[a][2].lstrip(), listParcels[a][3].lstrip(),
                                    listParcels[a][0].lstrip(), listDrones[b][0].lstrip()])

                    #if it is it will update drones time
                    listDrones[b][3] = listParcels[a][3].lstrip()

                    #then update the date on the timetable list
                    writeTB[counter2][0:2] = timeD.checkTime(writeTB[counter2][0:2], listParcels[a][6])

                    listDrones[b][2:4] = writeTB[counter2][0:2]

                    #finally updates drones
                    updateDrones(listDrones, listParcels, a, b)

                else: #if the time of the drone is bigger
                    writeTB.append([listParcels[a][2].lstrip(), listDrones[b][3].lstrip(),
                                    listParcels[a][0].lstrip(), listDrones[b][0].lstrip()])
                    # it will just update drones
                    updateDrones(listDrones, listParcels, a, b)

                #counters for iteration
                counter += 1
                counter2 += 1

                #break the loop because the parcel was matched
                bole2 = False


            #end the loop if exceeds the list lenght and write cancel if no match was found

            b += 1
            if b == len(listDrones) and False in listBool and counter == counter1:
                writeFinal.append([listParcels[a][2].lstrip(), listParcels[a][3].lstrip(),
                                   listParcels[a][0].lstrip(), 'cancelled'])
                bole2 = False

        #this conditions may not be necessary
        a += 1
        if a == len(listParcels):
            bole1 = False
        elif a == len(listParcels) and counter != counter1:
            a = 0

    #the writeFinal list has the cancelled orders that will be on top of the matched orders

    return {'timetable': writeFinal + pr.sortingMaches(writeTB), 'drones': pr.reOrganizeDrones(listDrones)}


def updateDrones(listDrones, listParcels, a, b):
    """ 
    Function that updates list of lists of drones

    Requires: A list with technical information retrieved from matching
    parcels and drones
    Ensures: an updated list of lists of each drone if needed
    """
    listDrones[b][6] = listDrones[b][6] - ((listParcels[a][4]/1000)*2) # update the range
    listDrones[b][7] += (listParcels[a][4]/1000) * 2 # update the acumulated distance
    listDrones[b][2:4] = timeD.addTimeAsString(listDrones[b][2:4], listParcels[a][6]) # update/add the time

    # return drones by sorting as specified in the project
    return listDrones.sort(key = lambda listDrones: (listDrones[2], listDrones[3], -listDrones[6], listDrones[7], listDrones[0]))










