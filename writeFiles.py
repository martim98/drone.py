import readFiles as rf
import organize as org



def writeTimeTable(parcelsFile, dronesFile):
    file = open('timetableTest.txt', 'w')
    for item in rf.readHeader(parcelsFile):
        file.write(str(item) + '\n')
    file.write('Timeline:' + '\n')
    for item in org.match(parcelsFile, dronesFile):
        for i in item:
            file.write(str(i) + ' ')
        file.write('\n')

    file.close()

writeTimeTable('parcels11h00_2019y11m5.txt', 'drones11h00_2019y11m5.txt')

