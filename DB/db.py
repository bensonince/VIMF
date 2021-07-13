from DBConnection import *

#brings back all Vollys as a complete list with summary information
def list_all_vollys():
    #put for loop code here
    vollys = db_list_vollys()
    return (vollys)

#brings back all Vollys for a particular shift
def list_all_vollys_for_shift(shiftID):
    shift_vollys = db_list_shift_vollys(shiftID = shiftID)
    return (shift_vollys)

#Retrieves a single Volly with all their details
def read_volly(vollyID):
    volly = db_read_volly(vollyID = vollyID)
    return (volly)

#Bring back all shifts with just the name of the
def listAllShifts():
     #put for loop code here
     shifts = db_list_shifts()
     return (shifts)

#Brings back a single Volly nd all their assigned shifts, and if they have attended a shift or not and any extra hours they may have done
def list_all_shifts_for_volly(vollyID):
     #put for loop code here
     volly_shifts = db_list_volly_shifts(vollyID = vollyID)
     return (volly_shifts)
     
#Retrieves a single shift with all its details
def read_shift(shiftID):
    shift = db_read_shift(shiftID = shiftID)
    return (shift)
