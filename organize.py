import readFiles as rf
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
        for i in range(-1, -7, -1):
            dronesOgranized.append(a[b][i])
        dronesOgranized.remove(dronesOgranized[2]) #remove hour
        dronesOgranized.remove(dronesOgranized[2]) #remove date
        dronesOgranized.insert(2, a[b][6])
        dronesOgranized.insert(3, a[b][7])
        orgOutListD.append(dronesOgranized)

    return orgOutListD

def checkInformation(fileName1, fileName2):
    list1 = rf.readParcelsFile(fileName1)
    list2 = organizeDrones(fileName2)
    print(list1, list2)
    print(len(list1[0]), len(list2[0]))


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







print(organizeDrones('drones11h30_2019y11m5.txt'))


