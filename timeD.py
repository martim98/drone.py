import datetime


def takeTime(time):
    """
    Function that reads time from the line and splits it into
    an hour and a minute parts

    Requires: time format in string ex: '12:30'
    Ensures: an int for an hour and an int for minutes, ex: 12, 9, 30
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
    Ensures: an int for a year, an int for a month and an
    int for a day, ex: 2019, 11, 1
    """
    string = date.replace(' ', '')
    y = string[0:4]
    m = string[5:7]
    d = string[8:10]
    assert int(y) >= 2000 and int(y) <= 2999
    assert int(m) >= 1 and int(m) <= 12
    assert int(d) >= 1 and int(d) <= 31

    return int(y), int(m), int(d)


def giveDateTime(str1, str2):
    """
    Converts time information retrieved from files into
    a datetime module format

    Requires: two string in the following format and order:
        'yyyy-mm-dd' 'hh:mm'
    Ensures: a datetime format of the input information
    """
    strf = str1.lstrip() + ' ' + str2.lstrip()
    date = datetime.datetime.strptime(strf, '%Y-%m-%d %H:%M')
    return date



def addTime(listTime, delta):
    """
    Add time to drones to update their information

    Requires: a list with two strings of date and hour in format 'yyyy-mm-dd' 'hh:mm'
    and a delta given by parcels information: int >= 0
    Ensures: A tuple with the times updated in two differente formats:
    one in a list in the same format as the input
    the second in datetime format
    """
    dateValidate = giveDateTime(listTime[0], listTime[1])
    delta = datetime.timedelta(minutes = delta)
    date = dateValidate + delta

    return ([date.strftime('%Y-%m-%d'), date.strftime('%H:%M')], date)

def convertTime(listTime):
    """
    Retrives the 20:00 hour of the day given
    ex: input list ['2019-05-03', '12:30']
    output list ['2019-05-03', '20:00']

    Requires: a list with strings of date and time
    Ensures: a new list with strings of the same date but with '20:00' as time
    """
    a = giveDateTime(listTime[0], listTime[1])
    return datetime.datetime(a.year, a.month, a.day, hour = 20, minute = 0)


def returnNewDate(listTime):
    """
    Calculates the '08:00' hour of next day
    ex: input list ['2019-05-03', '12:30']
    output list ['2019-05-04', '08:00']

	Requires: a list with date in yyyy-mm-dd format and hour
	in hh:mm
    Ensures: a list with strings of new date and hour in same format
    """
    b = giveDateTime(listTime[0], listTime[1])
    delta = datetime.timedelta(days = 1)
    b = datetime.datetime(b.year, b.month, b.day, hour = 8, minute = 0) + delta

    return [b.strftime('%Y-%m-%d'), b.strftime('%H:%M')]



