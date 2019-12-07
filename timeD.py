import datetime


def giveDateTime(str1, str2):
    strf = str1.lstrip() + ' ' + str2.lstrip()
    date = datetime.datetime.strptime(strf, '%Y-%m-%d %H:%M')
    return date

def addTime(list, delta):
    dateValidate = giveDateTime(list[0], list[1])
    delta = datetime.timedelta(minutes = delta)
    deltaIf = datetime.timedelta(days = 1)
    date = dateValidate + delta


    return [date.strftime('%Y-%m-%d'), date.strftime('%H:%M')]




