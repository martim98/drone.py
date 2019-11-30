def convertTime(string):
    string = string.replace(' ', '')
    new = string[0:2] + string[3:]

    return int(new)


def convertStrDrones(listA):
    for b in range(len(listA)):
        for i in range(3, 8):
            if i != 3:
                listA[b][i] = float(listA[b][i].strip())
            else:
                listA[b][i] = convertTime(listA[b][i])
    return listA


def convertStrParcles(listB):
    for b in range(len(listB)):
        for i in range(3, 7):
            if i != 3:
                listB[b][i] = float(listB[b][i].strip())
            else:
                listB[b][i] = convertTime(listB[b][i])
    return listB
