import datetime

def convertTime(string):
    """
    Function that converts a time into a 4 digit int

    Requires: a time format in string ex: '12:30'
    Ensures: a 4 digit int, ex: 1230
    """
    string = string.replace(' ', '')
    new = string[0:2] + string[3:]

    return int(new)


def takeTime(time):
    """
    Function that reads time from the line and splits it into
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


def giveDateTime(str1, str2):
    """
    Converts time information retrieved from files into
    a datetime module format

    Requires: two string in the following format and order:
        'year-month-day' 'hour:minutes'
    Ensures: a datetime format of the input information
    """
    strf = str1.lstrip() + ' ' + str2.lstrip()
    date = datetime.datetime.strptime(strf, '%Y-%m-%d %H:%M')
    return date
    #returns a datetime format than can support time operations
    


def addTimeAsString(list1, delta):
    """
    Add time to drones to update their information

    Requires: the lists of lists of drones and a delta given by parcels information: int >= 0
    Ensures: The list of lists of the drones with time information updated
    """
    dateValidate = giveDateTime(list1[0], list1[1])
    delta = datetime.timedelta(minutes = delta)
    date = dateValidate + delta

    return ([date.strftime('%Y-%m-%d'), date.strftime('%H:%M')], date)
    #this return a list with strings of date and time updated
    #ex: ['2019-06-01', '10:30']


def convertTime(list1):
    """
    Retrives the 20:00 hour of the day given
    ex: input list ['2019-05-03', '12:30']
    output list ['2019-05-03', '20:00']

    Requires: a list with strings of date and time
    Ensures: a new list with strings of the same date but with '20:00' as time
    """
    a = giveDateTime(list1[0], list1[1])
    return datetime.datetime(a.year, a.month, a.day, hour = 20, minute = 0)

def returnNewDate(list1):
    """
    Calculates the '08:00' of next day

    Requires: a list with two strings of date and hour
    returns: a list with strings of new date and hour
    """

    b = giveDateTime(list1[0], list1[1])
    delta = datetime.timedelta(days = 1)
    b = datetime.datetime(b.year, b.month, b.day, hour = 8, minute = 0) + delta

    return [b.strftime('%Y-%m-%d'), b.strftime('%H:%M')]



