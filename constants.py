
def convertTime(string):
    """ Function that converts a time into a 4 digit int
    Requires: a time format in string ex: '12:30'
    Ensures: a 4 digit int, ex: 1230
    """
    string = string.replace(' ', '')
    new = string[0:2] + string[3:]

    return int(new)


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
    assert int(h) >= 0 and int(h) <= 23
    assert int(m) >= 0 and int(m) <= 59
    
    return int(h), int(m)


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
    assert int(y) >= 2018
    assert m >= "01" and m <= "12"
    assert int(d) >= 1 and int(d) <= 31
    
    return int(y), int(m), int(d)



#x = takeTime("12:30")

def convertStrDrones(listA):
    """ Function that converts invalid types of drone list of list into valid
    Requires: a list of lists of the drones
    Ensures: A list of lists with numeric values as floats and time as a 4 digit int
    """
    for b in range(len(listA)):
        for i in range(3, 8):
            if i != 3:
                listA[b][i] = float(listA[b][i].strip())
            else:
                listA[b][i] = '{:02d}'.format(takeTime(listA[b][i])[0])+':{:02d}'.format(takeTime(listA[b][i])[1])
    return listA

#for b in range(len(listA)):
#        for i in range(len(listA[b])):
#            if i < 3:
#                pass
#            elif i > 3:
#                listA[b][i] = float(listA[b][i].strip())
#            else:
#                listA[b][i] = '{:02d}'.format(takeTime(listA[b][i])[0])+':{:02d}'.format(takeTime(listA[b][i])[1])
#    return listA

def convertStrParcles(listB):
    """ Function that converts invalid types of parcels list of list into valid
    Requires: a list of list of the parcels
    Ensures: A list of lists with numeric values as floats and time as a 4 digit int
    """
    for b in range(len(listB)):
        for j in range(len(listB[b])):
            listB[b][j] = listB[b][j].lstrip()
        for i in range(3, 7):
            if i != 3:
                listB[b][i] = float(listB[b][i].strip())
            else:
                listB[b][i] = '{:02d}'.format(takeTime(listB[b][i])[0])+':{:02d}'.format(takeTime(listB[b][i])[1])
        
    return listB

#x = rf.readParcelsFile('parcels16h00_2019y11m5.txt')
#csp = convertStrParcles(x)





