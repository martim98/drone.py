
def convertStrDrones(listA):
    """ Function that converts invalid types of drone list of list into valid
    Requires: a list of list of the drones
    Ensures: A list of lists with numeric values as ints and time as a 4 digit int
    """
    for b in range(len(listA)):
        for i in range(8):
            if i < 4:
                listA[b][i] = listA[b][i].lstrip()
            else:
                listA[b][i] = float(listA[b][i].strip())
    return listA

def convertStrParcles(listB):
    """ Function
    """
    for b in range(len(listB)):
        for i in range(7):
            if i < 4:
                listB[b][i] = listB[b][i].lstrip()
            else:
                listB[b][i] = float(listB[b][i].strip())
    return listB




