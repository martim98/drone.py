# 2019-2020 Fundamentos de Programação
# Grupo N
# número nome
# número nome

import sys
import readFiles as rf
import writeFiles as wf

inputFileName1, inputFileName2 = sys.argv[1:]

def allocate(fileNameDrones, fileNameParcels):
    """
    Assign given drones to given parcels.

    Requires: fileNameDrones, fileNameParcels are str, with the names
    of the files representing the list of drones and parcels, respectively,
    following the format indicated in the project sheet.
    Ensures: Two output files, respectively, with the listing of scheduled
    transportation of parcels and the updated listing of drones, following the format
    and naming convention indicated in the project sheet.
    """
#    if False in rf.checkInternal(fileNameDrones, fileNameParcels)[0]:
#        print('Input error: Name and header inconsistent in file(s) {}, {}!'.format(rf.checkInternal(fileNameDrones, fileNameParcels)[1][0], \
#                                                                 rf.checkInternal(fileNameDrones, fileNameParcels)[1][1]))
#    elif not rf.checkTitles(fileNameParcels, fileNameDrones):
#        print('Input error: Inconsistent files {} and {}'.format(fileNameParcels, fileNameDrones))
#    else:
#        wf.writeDrones(fileNameParcels, fileNameDrones)
#        wf.writeTimetable(fileNameParcels, fileNameDrones)
    rf.checkInternal(fileNameDrones, fileNameParcels)
    rf.checkTitles(fileNameParcels, fileNameDrones)
    wf.writeDrones(fileNameParcels, fileNameDrones)
    wf.writeTimetable(fileNameParcels, fileNameDrones)
        

allocate(inputFileName1, inputFileName2)

#allocate('drones19h30_2019y11m5.txt', 'parcels19h30_2019y11m5.txt')
#title_out = "timetable{0}h{1}_{2}y{3}m{4}.txt".format()
#newListA = open(title_out)







