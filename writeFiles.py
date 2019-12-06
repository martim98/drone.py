import readFiles as rf
import organize as org



def writeTimeTable(parcelsFile, dronesFile):
    """ Function that writes time table
    Requires: two txt input files as specified
    Ensures: a output txt file with the timetable
    """
    try:
        file = open('timetableTest.txt', 'w')
        for item in rf.readHeader(parcelsFile):
            file.write(str(item) + '\n')
        file.write('Timeline:' + '\n')
        for item in org.match(parcelsFile, dronesFile):
            print(item)
            for i in item:
                file.write(str(i) + ' ')
            file.write('\n')
        file.close()
    except IOError:
        print('ERROR: File not found')

writeTimeTable('parcels19h30_2019y11m5.txt', 'drones19h30_2019y11m5.txt')


def writeDronesUpdate(dronesFile):
    """Function that writes drone update file
    Requires: the drone input file as specified
    Ensures: a output txt file with the drone list updated after matching with parcels
    """



