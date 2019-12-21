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
    

def convertStrDrones(listDrones):
    """
    Function that converts invalid types of drone list of list into valid

    Requires: a list of lists of the drones
    Ensures: A list of lists with numeric values as floats and time as a 4 digit int
    """
    listDrones = removeEmpty(listDrones)
    for b in range(len(listDrones)):
        for j in range(len(listDrones[b])):
            listDrones[b][j] = listDrones[b][j].lstrip()
        for i in range(2, 4):
            listDrones[b][i] = int(listDrones[b][i])
        for i in range(4, 6):
            listDrones[b][i] = float(listDrones[b][i])
        listDrones[b][ct.D_HOUR] = '{:02d}:{:02d}'.format(timeD.takeTime(listDrones[b][ct.D_HOUR])[0], \
             timeD.takeTime(listDrones[b][ct.D_HOUR])[1])
    
    return listDrones


def convertStrParcels(listParcels):
    """
    Function that converts invalid types of parcels list of list into valid

    Requires: a list of list of the parcels
    Ensures: A list of lists with numeric values as floats and time as a 4 digit int
    """
    listParcels = removeEmpty(listParcels)
    for b in range(len(listParcels)):
        for j in range(len(listParcels[b])):
            listParcels[b][j] = listParcels[b][j].lstrip()
        listParcels[b][ct.P_DISTANCE] = int(listParcels[b][ct.P_DISTANCE])
        for i in range(5, 7):
            if i != ct.P_HOUR:
                listParcels[b][i] = float(listParcels[b][i].strip())
            else:
                listParcels[b][i] = '{:02d}:{:02d}'.format(timeD.takeTime(listParcels[b][i])[0], \
                     timeD.takeTime(listParcels[b][i])[1])

    return listParcels
