import readFiles as rf
import operations as op
import constants as ct
import timeD

def sortTimetable(timetable):
    """
    Function that sorts the output timetable in an
    expected order and puts first the cancelled orders
    Order: first places the cancelled orders in
    time-ascending order, then by name; then place matched
    orders by date, time, name
    
    Requires: a list of lists of matched orders
    Ensures: a sorted list of lists of matched orders
    """
    timetable.sort(key = lambda x: (x[ct.T_DATE], x[ct.T_HOUR], x[ct.T_PARCEL]))
    counter = 0
    for i in range(len(timetable)):
        if 'cancelled' in timetable[i][ct.T_STATUS]:
            timetable.insert(0, timetable.pop(i))
            counter += 1
    csort = sorted(timetable[0:counter], key = lambda x: (x[ct.T_HOUR], x[ct.T_PARCEL]))
    csort.extend(timetable[counter:])

    return csort

def updateDrones(listD, listP, a, b):
    """
    Function that updates list of lists of drones

    Requires: the two lists of lists of drones and parcels, the a index of parcels
    and the b index of the drones
    Ensures: an updated list of lists of each drone if needed
    """
    #Updating Drones as specified in the project
    listD[b][ct.D_RANGE] -= ((listP[a][ct.P_DISTANCE]/1000)*2)
    listD[b][ct.D_ACUM_DISTANCE] += (listP[a][ct.P_DISTANCE]/1000)*2
    listD[b][ct.D_DATE:] = timeD.addTime(listD[b][ct.D_DATE:], listP[a][ct.P_TIME])[ct.AS_STRING]

    #return drones by sorting as specified in the project
    return listD.sort(key = lambda x: (x[ct.D_DATE], x[ct.D_HOUR], -x[ct.D_RANGE],
                                           x[ct.D_ACUM_DISTANCE], x[ct.D_NAME]))


def match(fileNameParcels, fileNameDrones):
    """
    The core function, it matches drones with parcels

    Requires: two fileNames of parcels and drones in this order
    Ensures: A list of list of the parcels matched with the drones (timetable list) and the updated
    drones list
    """
    listD = op.convertStrDrones(rf.readListing(fileNameDrones))
    listP = op.convertStrParcels(rf.readListing(fileNameParcels))
    listD.sort(key= lambda x: (x[ct.D_DATE], x[ct.D_HOUR], -x[ct.D_RANGE],
                                 x[ct.D_ACUM_DISTANCE], x[ct.D_NAME]))
    writeTB = []
    for a in range(len(listP)):
        h = True
        b = 0
        while h:
            # Comparing information from Drones and Parcels, if every condition is met, proceed in code, 
            # if not, break the loop and iterate over the next drone
            if (listP[a][ct.P_DATE] == listD[b][ct.D_DATE])\
                    and listP[a][ct.P_ZONE] == listD[b][ct.D_ZONE] \
                    and listP[a][ct.P_DISTANCE] <= listD[b][ct.D_MAX_DISTANCE]\
                    and listP[a][ct.P_DISTANCE]*2-listD[b][ct.D_RANGE]*1000 <= ct.DELTA_FLOATS \
                    and listP[a][ct.P_WEIGHT] <= listD[b][ct.D_WEIGHT]:
                # The order time must be the biggest time between drone and parcel
                maksimum = max(listD[b][ct.D_HOUR], listP[a][ct.P_HOUR])
                listD[b][ct.D_HOUR] = maksimum
                time = [listD[b][ct.D_DATE], maksimum]

                # Condition to check if the order ends after 20h00
                if timeD.addTime(time, listP[a][ct.P_TIME])[ct.AS_DATETIME] <= timeD.convertTime(time):
                    writeTB.append([listP[a][ct.P_DATE], maksimum, listP[a][ct.P_NAME], listD[b][ct.D_NAME]])
                else:
                    writeTB.append(timeD.returnNewDate(time) + [listP[a][ct.P_NAME], listD[b][ct.D_NAME]])
                    listD[b][ct.D_DATE:] = timeD.returnNewDate(time)

                h = False
                updateDrones(listD, listP, a, b)
            else:
                # Else: if every drone was checked and no match was found, then cancel the order
                if b == len(listD)-1:
                    writeTB.append([listP[a][ct.P_DATE], listP[a][ct.P_HOUR], listP[a][ct.P_NAME], "cancelled"])
                    h = False
            b +=1

    writeTBsorted = sortTimetable(writeTB)
    return listD, writeTBsorted



