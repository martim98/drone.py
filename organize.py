import readFiles as rf
from copy import deepcopy

def organizeInd():
    """
    This module receives information retrived from the readfiles and outputs lists
    with organized information for the timetable file
    """


def organizeDrones(fileName):
    a = rf.readDronesFile(fileName)
    orgOutListD = []
    for b in range(len(a)):
        dronesOgranized = []
        for i in range(0, 2):
            dronesOgranized.append(a[b][i])
        for i in range(0, -7, -1):
            dronesOgranized.append(a[b][i])
        dronesOgranized.remove(dronesOgranized[2])
        dronesOgranized.remove(dronesOgranized[3]) #remove date
        dronesOgranized.remove(dronesOgranized[2]) #remove hour
        dronesOgranized.insert(2, a[b][6])
        dronesOgranized.insert(3, a[b][7])
        orgOutListD.append(dronesOgranized)

    return orgOutListD









print(organizeDrones('drones11h30_2019y11m5.txt'))


