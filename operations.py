import timeD
import constants as ct


def removeEmpty(any_list):
    """
    Function that makes sure thet there are no [''] in the output list
    Requires: a list of lists of lines
    Ensures: a list of lists of lines without ['']
    """
    while [''] in any_list: 
        any_list.remove([''])
    return any_list
    

def convertStrDrones(listA):
    """
    Function that converts invalid types of drone list of list into valid

    Requires: a list of lists of the drones
    Ensures: A list of lists with numeric values as floats and time as a 4 digit int
    """
    listA = removeEmpty(listA)
    for b in range(len(listA)):
        for j in range(len(listA[b])):
            listA[b][j] = listA[b][j].lstrip()
        for i in range(2, 4):
            listA[b][i] = int(listA[b][i])
        for i in range(4, 6):
            listA[b][i] = float(listA[b][i])
        listA[b][ct.D_HOUR] = '{:02d}:{:02d}'.format(timeD.takeTime(listA[b][ct.D_HOUR])[0], \
             timeD.takeTime(listA[b][ct.D_HOUR])[1])
    
    return listA


def convertStrParcels(listB):
    """
    Function that converts invalid types of parcels list of list into valid

    Requires: a list of list of the parcels
    Ensures: A list of lists with numeric values as floats and time as a 4 digit int
    """
    listB = removeEmpty(listB)
    for b in range(len(listB)):
        for j in range(len(listB[b])):
            listB[b][j] = listB[b][j].lstrip()
        listB[b][ct.P_DISTANCE] = int(listB[b][ct.P_DISTANCE])
        for i in range(5, 7):
            if i != ct.P_HOUR:
                listB[b][i] = float(listB[b][i].strip())
            else:
                listB[b][i] = '{:02d}:{:02d}'.format(timeD.takeTime(listB[b][i])[0], \
                     timeD.takeTime(listB[b][i])[1])

    return listB
