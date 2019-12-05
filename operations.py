
def convertTime(string):
    """ Function that converts a time into a 4 digit int
    Requires: a time format in string ex: '12:30'
    Ensures: a 4 digit int, ex: 1230
    """
    string = string.replace(' ', '')
    new = string[0:2] + string[3:]

    return int(new)

def convertStrDrones(listA):
    """ Function that converts invalid types of drone list of list into valid
    Requires: a list of list of the drones
    Ensures: A list of lists with numeric values as ints and time as a 4 digit int
    """
    for b in range(len(listA)):
        for i in range(3, 8):
            if i != 3:
                listA[b][i] = float(listA[b][i].strip())
            else:
                listA[b][i] = convertTime(listA[b][i])
    return listA

def convertStrParcles(listB):
    """ Function
    """
    for b in range(len(listB)):
        for i in range(3, 7):
            if i != 3:
                listB[b][i] = float(listB[b][i].strip())
            else:
                listB[b][i] = convertTime(listB[b][i])
    return listB


def convertTimeToStr(int):
    """ Function that converts a time into a 4 digit int
    Requires: a time format in string ex: '12:30'
    Ensures: a 4 digit int, ex: 1230
    """
    strInt = str(int)
    return strInt[0:2] + ':' + strInt[2:]

