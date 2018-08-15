
def convertOffsetToJulian(offsetDateList, year): # convert offset date to julian
    julianDateList = []
    for count, offsetDate in enumerate(offsetDateList): 
        if year % 4 == 0:
            daysInYear = 366
            offsetStartDate = 274
        else: 
            daysInYear = 365
            offsetStartDate = 273
          
        intOffsetDate = int(offsetDate)
        
        
        if intOffsetDate <=  offsetStartDate:
            julian_nonoffset_date = intOffsetDate + (daysInYear - offsetStartDate)
            julianDateList.append(julian_nonoffset_date)
        else:
            julian_nonoffset_date = intOffsetDate - offsetStartDate
            julianDateList.append(julian_nonoffset_date)
        
    return julianDateList 
