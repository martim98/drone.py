
def convertTime(string):
    """ Function that converts a time into a 4 digit int
    Requires: a time format in string ex: '12:30'
    Ensures: a 4 digit int, ex: 1230
    """
    string = string.replace(' ', '')
    new = string[0:2] + string[3:]

    return int(new)

#####delete??
def takeTime(time):
    """Function that reads time from the line and splits it into
    an hour and a minute parts
    Requires: time format in string ex: '12:30'
    Ensures: a two digit int for an hour, ex: 12, 09, and 
    a two digit int for minutes, ex: 30
    """
    string = time.replace(' ', '')
    h = string[0:2]
    m = string[3:5]
#    assert h >= 0 and h <= 23
#    assert m >= 0 and m <= 59
    
    return int(h), int(m)

#####delete??
def takeDate(date):
    """
    Function that reads date as string from the line and splits it into
    a day, a month and a year parts
    
    Requires: date format in string in yyyy, mm, dd order, ex: '2019-11-01'
    Ensures: a four digit int for a year, two digit int for a month and one
    digit int for a day, ex: 2019, 11, 1
    """
    string = date.replace(' ', '')
    y = string[0:4]
    m = string[5:7]
    d = string[8:10]
    
    return int(y), int(m), int(d)



#x = takeTime("12:30")

def convertStrDrones(listA):
    """ Function that converts invalid types of drone list of list into valid
    Requires: a list of lists of the drones
    Ensures: A list of lists with numeric values as floats and time as a 4 digit int
    """
    for b in range(len(listA)):
        for j in range(len(listA[b])):
            listA[b][j] = listA[b][j].lstrip()
        for i in range(2, 4):
            listA[b][i] = int(listA[b][i])
        for i in range(4,6):
            listA[b][i] = float(listA[b][i])
        listA[b][7] = '{:02d}'.format(takeTime(listA[b][7])[0])+':{:02d}'.format(takeTime(listA[b][7])[1])
    while [''] in listA: # this code is just to be sure that there are no [''] in the output list
        listA.remove([''])
    return listA

def convertStrParcles(listB):
    """
    Function that converts invalid types of parcels list of list into valid

    Requires: a list of list of the parcels
    Ensures: A list of lists with numeric values as floats and time as a 4 digit int
    """
    for b in range(len(listB)):
        for j in range(len(listB[b])):
            listB[b][j] = listB[b][j].lstrip()
        listB[b][4] = int(listB[b][4])
        for i in range(5, 7):
            if i != 3:
                listB[b][i] = float(listB[b][i].strip())
            else:
                listB[b][i] = '{:02d}'.format(takeTime(listB[b][i])[0])+':{:02d}'.format(takeTime(listB[b][i])[1])
    while [''] in listB: # this code is just to be sure that there are no [''] in the output list
        listB.remove([''])

    return listB







