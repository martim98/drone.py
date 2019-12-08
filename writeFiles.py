import readFiles as rf
import organize as org



def writeTimeTable(parcelsFile, dronesFile):
    """
    Writes time table
    Requires: two txt input files as specified
    Ensures: a output txt file with the timetable
    """
    try:
        file = open('timetableTest.txt', 'w')
        for item in rf.readHeader(parcelsFile):
            file.write(str(item) + '\n')
        file.write('Timeline:' + '\n')
        for item in org.match(parcelsFile, dronesFile)['timetable']:
            counter = 0
            for i in item:
                if counter < 3:
                    file.write(str(i) + ', ')
                else:
                    file.write(str(i))

                counter += 1
            file.write('\n')
        file.close()
    except IOError:
        print('ERROR: File not found')




def writeDronesUpdate(parcelsFile, dronesFile):
    """
    Writes drone update file

    Requires: the drone input file as specified
    Ensures: a output txt file with the drone list updated after matching with parcels
    """
    file = open('droneWRITE.txt', 'w')
    for item in rf.readHeader(parcelsFile):
        file.write(str(item) + '\n')
    file.write('Drones:' + '\n')
    for item in org.match(parcelsFile, dronesFile)['drones']:
        counter = 0
        for i in item:
            if counter < 7:
                file.write(str(i) + ', ')
            else:
                file.write(str(i))
            counter += 1
        file.write('\n')
    file.close()


writeTimeTable('parcels19h30_2019y11m5.txt', 'drones19h30_2019y11m5.txt')
writeDronesUpdate('parcels19h30_2019y11m5.txt', 'drones19h30_2019y11m5.txt')




