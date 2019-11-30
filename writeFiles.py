import readFiles as rf
import organize as org


a = rf.readHeader('parcels15h30_2019y11m4.txt')
file = open('timetable.txt', 'w')
for item in a:
    file.write(item + '\n')
a = org.checkInformation('parcels15h30_2019y11m4.txt', 'drones15h30_2019y11m4.txt')
file.write(a[0][0] + ', ' + str(a[0][1]) + ', ' + a[0][2] + ', ' +  a[0][3])

file.close()