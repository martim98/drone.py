import readFiles as rf
import operations as op
import timeD

def sortTimetable(timetable):
    """
    Function that sorts the output timetable in an
    expected order and puts first the cancelled orders
    Order: first place the cancelled orders in
    time-ascending order, then by name; then place matched
    orders by date, time, name
    
    Requires: a list of lists of matched orders
    Ensures: a sorted list of lists of matched orders
    """
    timetable.sort(key = lambda x: (x[0], x[1], x[2]))
    counter = 0
    for i in range(len(timetable)):
        if 'cancelled' in timetable[i][3]:
            timetable.insert(0, timetable.pop(i))
            counter += 1
    csort = sorted(timetable[0:counter], key = lambda x: (x[1], x[2]))
    csort.extend(timetable[counter:])
    return csort

def updateDrones(listDrones, listParcels, a, b):
    """
    Function that updates list of lists of drones

    Requires: the two lists of lists of drones and parcels, the a index of parcels
    and the b index of the drones
    Ensures: an updated list of lists of each drone if needed
    """
    listDrones[b][5] -= ((listParcels[a][4]/1000)*2) # update the range
    listDrones[b][4] += (listParcels[a][4]/1000) * 2 # update the acumulated distance
    listDrones[b][6:8] = timeD.addTimeAsString(listDrones[b][6:8], listParcels[a][6])[0] # update/add the time

    # return drones by sorting as specified in the project
    return listDrones.sort(key = lambda listDrones: (listDrones[6], listDrones[7], listDrones[5], -listDrones[4], listDrones[0]))

def match(fileName1, fileName2):
    """
    The core function, it matches drones with parcels

    Requires: two fileNames of parcels and drones in this order
    Ensures: A list of list of the drones matched with drones
    """
    listD = op.convertStrDrones(rf.readListing(fileName2))
    listP = op.convertStrParcles(rf.readListing(fileName1))
    listD.sort(key= lambda listD: (listD[6], listD[7], listD[5], -listD[4], listD[0]))
    writeTB = []
    for a in range(len(listP)):
        h = True
        b = 0
        while h:
            #date:
            if (listP[a][2] == listD[b][6]) and listP[a][1] == listD[b][1] \
                    and listP[a][4] <= listD[b][3] and listP[a][4] < listD[b][3]*1000 \
                    and listP[a][5] <= listD[b][2]:
                #hour: if listP[a][3] >= listD[b][3]:
                #zone and distance and autonomy:
                #weight:
                maksimum = max(listD[b][7], listP[a][3])
                listD[b][7] = maksimum
                time = [listD[b][6], maksimum]

                if timeD.addTimeAsString(time, listP[a][6])[1] <= timeD.convertTime(time):
                    writeTB.append([listP[a][2], maksimum, listP[a][0], listD[b][0]])

                else:
                    writeTB.append(timeD.returnNewDate(time) + [listP[a][0], listD[b][0]])
                    listD[b][6:8] = timeD.returnNewDate(time)
                h = False
                updateDrones(listD, listP, a, b)

            else:
                if b == len(listD)-1:
                    writeTB.append([listP[a][2], listP[a][3], listP[a][0], "cancelled"])
                    h = False
            b +=1
    writeTBsorted = sortTimetable(writeTB)

    return listD, writeTBsorted



