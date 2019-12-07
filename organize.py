import readFiles as rf
import operations as op
import timeD
from copy import deepcopy


def organizeDrones(fileName):
    """ Function that reorganizes list of lists of drones
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
    """Function to organize and prepare list of lists of parcels
    requires: the fileName of parcels
    ensures: A list of list with values adpted for further functions
    """
    parcelsOrganized = rf.readParcelsFile(fileName)
    while [''] in parcelsOrganized:
        parcelsOrganized.remove([''])
    return op.convertStrParcles(parcelsOrganized)

def match(fileName1, fileName2):
    """The core function, it matches drones with parcels
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
    while bole1:
        bole2 = True
        b = 0
        counter1 = counter
        while bole2:
            listBool = []
            for i in range(1, 3):
                listBool.append(listParcels[a][i] == listDrones[b][i])
            for i in range(4, 6):
                listBool.append(listDrones[b][i] >= listParcels[a][i])
            listBool.append(listDrones[b][6]*1000 > listParcels[a][4]) #distance
            listF.append(listBool)

            # checking the booleans and matching
            if False not in listBool:
                if timeD.giveDateTime(listDrones[b][2], listDrones[b][3]) <= timeD.giveDateTime(listParcels[a][2], listParcels[a][3]):
                    writeTB.append([listParcels[a][2].lstrip(), listParcels[a][3].lstrip(),
                                    listParcels[a][0].lstrip(), listDrones[b][0].lstrip()])
                    listDrones[b][3] = listParcels[a][3].lstrip()
                    updateDrones(listDrones, listParcels, a, b)

                else:
                    writeTB.append([listParcels[a][2].lstrip(), listDrones[b][3].lstrip(),
                                    listParcels[a][0].lstrip(), listDrones[b][0].lstrip()])
                    updateDrones(listDrones, listParcels, a, b)


                counter += 1
                bole2 = False

            #end the loop if exceeds the list lenght and write cancel if no match was found

            b += 1
            if b == len(listDrones) and False in listBool and counter == counter1:
                writeFinal.append([listParcels[a][2].lstrip(), listParcels[a][3].lstrip(),
                                   listParcels[a][0].lstrip(), 'cancelled'])
                bole2 = False




        a += 1
        if a == len(listParcels):
            bole1 = False
        elif a == len(listParcels) and counter != counter1:
            a = 0


    return {'timetable': writeFinal + writeTB, 'drones': listDrones}





def updateDrones(listDrones, listParcels, a, b):
    """ Function that updates list of lists of drones
    Requires: A list with technical information retrieved from matching
    parcels and drones
    Ensures: an updated list of lists of each drone if needed
    """
    listDrones[b][6] = listDrones[b][6] - ((listParcels[a][4]*2)/1000)
    listDrones[b][7] += (listParcels[a][4]*2)
    listDrones[b][2:4] = timeD.addTime(listDrones[b][2:4], listParcels[a][6])


    return listDrones








