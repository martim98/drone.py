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
    #returns a datetime format than can support time operations

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
    #this return a list with strings of date and time updated
    #ex: ['2019-06-01', '10:30']

def addTimeAsDateTime(list, delta):
    """
    Add time to drones to update their information

    Requires: the lists of lists of drones and a delta given by parcels information: int >= 0
    Ensures: The list of lists of the drones with time information updated
    """
    dateValidate = giveDateTime(list[0], list[1])
    delta = datetime.timedelta(minutes = delta)
    date = dateValidate + delta

    return date
    #this returns the time updated but in a datetime format
    #it can be merged with the previous function



def checkTime(list1, delta):
    """
    Checks if the order finishes after 20:00
    and if so, returns a new date beginning in the next day at 8:00,
    if not, does nothing

    requires: a list with date and time as strings, and a delta, int => 0
    ensures: a list with two strings respectively of date and hour
    """
    if addTimeAsDateTime(list1, delta) > convertTime(list1):
        return returnNewDate(list1)
    else:
        return list1



def convertTime(list1):
    """
    Retrives the 20:00 hour of the day given
    ex: input list ['2019-05-03', '12:30']
    output list ['2019-05-03', '20:00']

    requires: a list with strings of date and time
    ensures: a new list with strings of the same date but with '20:00' as time
    """
    a = giveDateTime(list1[0],list1[1])
    return datetime.datetime(a.year, a.month, a.day, hour= 20, minute=0)

def returnNewDate(list1):
    """
    Calculates the '08:00' of next day

    requires: a list with two strings of date and hour
    returns: a list with strings of new date and hour
    """
    b = giveDateTime(list1[0], list1[1])
    delta = datetime.timedelta(days = 1)
    b =  datetime.datetime(b.year, b.month, b.day, hour = 8, minute = 0) + delta

    return [b.strftime('%Y-%m-%d'), b.strftime('%H:%M')]



