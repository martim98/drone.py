import readFiles as rf
import constants as ct
from copy import deepcopy



def organizeDrones(fileName):
    """ Function that reorganizes list of lists of drones
    Requires: A list of lists with the drone information retrieved
    from the readFiles.py function "readDronesFile()"
    Ensures: A list sorted in the same order of the list of lists
    of the parcels information
    """
    a = rf.readDronesFile(fileName)
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


    ct.convertStrDrones(orgOutListD)
    return orgOutListD

def organizeParcels(fileName):
    a = rf.readParcelsFile(fileName)
    ct.convertStrParcles(a)
    return a

def checkInformation(fileName1, fileName2):
    list1 = organizeParcels(fileName1)
    list2 = organizeDrones(fileName2)
    print(list1)
    print(list2)
    listF =[]
    writeTB = []
    for a in range(len(list1)):
        for b in range(len(list2)):
            listBool = []
            for i in range(1, 3):
                listBool.append(list1[a][i] == list2[b][i])
            for i in range(4, 6):
                listBool.append(list2[b][i] >= list1[a][i])

            listBool.append(list2[b][6]*1000 > list1[a][4]) # distance
            listBool.append(list2[b][3] <= list1[a][3]) # time
            listF.append(listBool)
            if False not in listBool:
                writeTB.append([list1[a][2], list1[a][3], list1[a][0], list2[b][0]])


        print(listF)
        print(writeTB)
        return writeTB







    """ Function that matches drones with parcels
    Requires: Two lists of lists, one from drones, other from parcels
    Ensures: A list of lists with the orders matched or canceled
    """

checkInformation('parcels15h30_2019y11m4.txt', 'drones15h30_2019y11m4.txt')


def updateDrones():
    """ Function that updates list of lists of drones
    Requires: A list with technical information retrieved from matching
    parcels and drones
    Ensures: an updated list of lists of each drone if needed
    """










