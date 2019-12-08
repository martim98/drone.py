import datetime


def giveDateTime(str1, str2):
    """
    Converts time information retrieved from files into
    a datetime module format

    Requires: two string in the format 'year-month-day' 'hour:minutes'
    Ensures: a datetime format of the input information
    """
    strf = str1.lstrip() + ' ' + str2.lstrip()
    date = datetime.datetime.strptime(strf, '%Y-%m-%d %H:%M')
    return date

def addTimeAsString(list, delta):
    """
    Add time to drones to update their information

    Requires: the lists of lists of drones and a delta given by parcels information: int >= 0
    Ensures: The list of lists of the drones with time information updated
    """
    dateValidate = giveDateTime(list[0], list[1])
    delta = datetime.timedelta(minutes = delta)
    deltaIf = datetime.timedelta(days = 1)
    date = dateValidate + delta

    return [date.strftime('%Y-%m-%d'), date.strftime('%H:%M')]

def addTimeAsDateTime(list, delta):
    """
    Add time to drones to update their information

    Requires: the lists of lists of drones and a delta given by parcels information: int >= 0
    Ensures: The list of lists of the drones with time information updated
    """
    dateValidate = giveDateTime(list[0], list[1])
    delta = datetime.timedelta(minutes = delta)
    deltaIf = datetime.timedelta(days = 1)
    date = dateValidate + delta

    return date



def checkTime(list1, delta):
    if addTimeAsDateTime(list1, delta) > convertTime(list1):
        return returnNewDate(list1)
    else:
        return list1


def convertTime(list1):
    a = giveDateTime(list1[0],list1[1])
    return datetime.datetime(a.year, a.month, a.day, hour= 20, minute=0)

def returnNewDate(list1):
    b = giveDateTime(list1[0], list1[1])
    delta = datetime.timedelta(days = 1)
    b =  datetime.datetime(b.year, b.month, b.day, hour = 8, minute = 0) + delta

    return [b.strftime('%Y-%m-%d'), b.strftime('%H:%M')]



