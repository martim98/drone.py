#Module to prepare files for the writeFiles
import math


def sortingMaches(list1):
    """
    Function that sorts matches list by time

    Requires: a match input list
    Ensures: a list chronological sorted
    """
    list1.sort(key= lambda list1: (list1[0], list1[1]))
    return list1

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



