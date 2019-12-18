import timeD

def convertStrDrones(listA): #
    """
    Function that converts invalid types of drone list of list into valid

    Requires: a list of lists of the drones
    Ensures: A list of lists with numeric values as floats and time as a 4 digit int
    """
    while [''] in listA: # this code is just to be sure that there are no [''] in the output list
        listA.remove([''])
    for b in range(len(listA)):
        for j in range(len(listA[b])):
            listA[b][j] = listA[b][j].lstrip()
        for i in range(2, 4):
            listA[b][i] = int(listA[b][i])
        for i in range(4, 6):
            listA[b][i] = float(listA[b][i])
        listA[b][7] = '{:02d}'.format(timeD.takeTime(listA[b][7])[0])+':{:02d}'.format(timeD.takeTime(listA[b][7])[1])

    return listA

def convertStrParcles(listB):
    """
    Function that converts invalid types of parcels list of list into valid

    Requires: a list of list of the parcels
    Ensures: A list of lists with numeric values as floats and time as a 4 digit int
    """
    while [''] in listB: # this code is just to be sure that there are no [''] in the output list
        listB.remove([''])
    for b in range(len(listB)):
        for j in range(len(listB[b])):
            listB[b][j] = listB[b][j].lstrip()
        listB[b][4] = int(listB[b][4])
        for i in range(5, 7):
            if i != 3:
                listB[b][i] = float(listB[b][i].strip())
            else:
                listB[b][i] = '{:02d}'.format(timeD.takeTime(listB[b][i])[0])+':{:02d}'.format(timeD.takeTime(listB[b][i])[1])
    while [''] in listB:
        listB.remove([''])

    return listB
