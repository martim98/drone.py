import readFiles as rf
import operations as op
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
    for a in range(len(listParcels)):
        bole = True
        b = 0
        while bole:
            listBool = []
            for i in range(1, 3):
                listBool.append(listParcels[a][i] == listDrones[b][i])
            for i in range(4, 6):
                listBool.append(listDrones[b][i] >= listParcels[a][i])
            listBool.append(listDrones[b][6]*1000 > listParcels[a][4]) # distance
            listBool.append(listDrones[b][3] <= listParcels[a][3]) # time
            listF.append(listBool)
            if False not in listBool:
                writeTB.append([listParcels[a][2].lstrip(), op.convertTimeToStr(listParcels[a][3]), listParcels[a][0], listDrones[b][0]])
                updateDrones(listDrones)
                bole = False
            b += 1
            if b == len(listDrones) - 1 and False in listBool:
                writeFinal.append([listParcels[a][2].lstrip(), op.convertTimeToStr(listParcels[a][3]), listParcels[a][0], listDrones[b][0], 'cancelled'])
                bole = False
            elif b == len(listDrones) - 1:
                bole = False






    return writeFinal + writeTB



def updateDrones(list):
    """ Function that updates list of lists of drones
    Requires: A list with technical information retrieved from matching
    parcels and drones
    Ensures: an updated list of lists of each drone if needed
    """
    return list







match('parcels15h30_2019y11m4.txt', 'drones15h30_2019y11m4.txt')

