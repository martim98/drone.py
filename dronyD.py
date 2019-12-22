# 2019-2020 Fundamentos de Programacao
# Grupo 30
# 54070 Kinga Bondyra
# 55066 Martim Almeida

import sys
import writeFiles as wf


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
    # When running the writeTimetable function, the program will call the readFiles functions
    # that assert the prerequisites
    wf.writeTimetable(fileNameParcels, fileNameDrones)
    wf.writeDrones(fileNameParcels, fileNameDrones)

fileNameDrones, fileNameParcels = sys.argv[1:]

allocate(fileNameDrones, fileNameParcels)









