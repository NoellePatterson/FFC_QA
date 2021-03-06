import numpy as np
from Utils.convertDateType import convertOffsetToJulian

def LSRspringBfl(classes):

    LSRspringBfl = {}
    LSRspringBflRate = {}
    allOtherYearsRate = {}
    for currentClass, value in classes.items():
        springTim = []
        sumTim = []
        for i, results in enumerate(value):
            springTim.append(value[i].loc['SP_Tim'])

        for i, results in enumerate(value):
            sumTim.append(value[i].loc['DS_Tim'])

        allWaterYears = 0
        counter = 0
        LSRspringBflRateArray = []
        allOtherYearsRateArray = []
        for index, gage in enumerate(springTim): # loop through each gage (223)
            year = int(gage.index[0])
            for i, year in enumerate(gage): # loop through each year in the gage
                allWaterYears = allWaterYears + 1
                if np.isnan(springTim[index][i]) == False and np.isnan(sumTim[index][i]) == False:
                    offsetSpringTim = [int(springTim[index][i])]
                    offsetSpringTim = convertOffsetToJulian(offsetSpringTim, year)

                    offsetSumTim = [int(sumTim[index][i])]
                    offsetSumTim = convertOffsetToJulian(offsetSumTim, year)
                    if offsetSpringTim[0] + 30 >= offsetSumTim[0]: # check when spring and summer are within 30 days of eachother
                        counter = counter + 1
                        LSRspringBflRateArray.append(None)
                        LSRspringBflRateArray[-1] = value[index].loc['SP_ROC'][i] # index the rate of change of that gage in that year
                    elif offsetSpringTim[0] + 30 < offsetSumTim[0]:
                        allOtherYearsRateArray.append(None)
                        allOtherYearsRateArray[-1] = value[index].loc['SP_ROC'][i] #index the rate of change of all other years

            if currentClass in LSRspringBfl:
                LSRspringBfl[currentClass].append(counter/allWaterYears)
                LSRspringBflRate[currentClass].append(np.nanmean(LSRspringBflRateArray))
                allOtherYearsRate[currentClass].append(np.nanmean(allOtherYearsRateArray))
            else:
                LSRspringBfl[currentClass] = [counter/allWaterYears]
                LSRspringBflRate[currentClass] = [np.nanmean(LSRspringBflRateArray)]
                allOtherYearsRate[currentClass] = [np.nanmean(allOtherYearsRateArray)]

    for currentClass in LSRspringBfl:
        LSRspringBfl[currentClass] = np.nanmean(LSRspringBfl[currentClass])
        LSRspringBflRate[currentClass] = np.nanmean(LSRspringBflRate[currentClass])
        allOtherYearsRate[currentClass] = np.nanmean(allOtherYearsRate[currentClass])

    return LSRspringBfl, LSRspringBflRate, allOtherYearsRate
