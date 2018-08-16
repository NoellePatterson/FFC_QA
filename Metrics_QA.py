import glob
import csv
import pandas as pd
from Utils.sortGages import sortGages
from Utils.importHighflowResults import importHighflowResults
from calculations.wetInitCount import wetInitCount
from calculations.wetCount import wetCount
from calculations.springBflLag import springBflLag
from calculations.snowEarly import snowEarly
from calculations.snowSpringBfl import snowSpringBfl
from calculations.LSRspringBfl import LSRspringBfl
from calculations.rainWetSpring import rainWetSpring
from calculations.rainZeroFlow import rainZeroFlow
from calculations.rainLateBfl import rainLateBfl
from calculations.rainEarlySpring import rainEarlySpring
from calculations.rainLateWet import rainLateWet
from calculations.LSRstandardDev import LSRstandardDev

files = glob.glob("All-Results/*_annual_result_matrix.csv")
highflowFiles = glob.glob("Highflow-Results/*_annual_result_matrix.csv") 

classes = sortGages(files)

allResults = classes['class1'] + classes['class2'] + classes['class3'] + classes['class4'] + classes['class5']+ classes['class6']+ classes['class7']+ classes['class8']+ classes['class9']
snowResults = classes['class1'] + classes['class2'] + classes['class9']
LSRresults = classes['class3']
rainResults = classes['class4'] + classes['class6'] + classes['class7'] + classes['class8']

highflowClasses = importHighflowResults(highflowFiles)
highflowRainResults = highflowClasses['class4'] + highflowClasses['class6'] + highflowClasses['class7'] + highflowClasses['class8']
highflowLSRresults = highflowClasses['class3'] 

wetInitCount = wetInitCount(classes)
wetCount = wetCount(classes)
springBflLag = springBflLag(classes)
snowEarlySpring, snowEarlyWet = snowEarly(classes) 
snowSpringBfl, snowSpringBflRate, allOtherYearsRate = snowSpringBfl(classes) 
LSRspringBfl, LSRspringBflRate, allOtherYearsRate = LSRspringBfl(classes) 
rainWetSpring = rainWetSpring(classes)
rainZeroFlow = rainZeroFlow(classes)
rainLateBfl = rainLateBfl(classes)
rainEarlySpring = rainEarlySpring(highflowClasses)
rainLateWet = rainLateWet(highflowClasses)
LSRstandardDev = LSRstandardDev(LSRresults)

'Results into CSV output'
with open('resultsOutput.csv', 'w') as csvfile:
    resultsWriter = csv.DictWriter(csvfile, wetInitCount.keys())
    resultsWriter.writeheader()
    resultsWriter.writerow(wetInitCount)
    resultsWriter.writerow(wetInitCount)
    resultsWriter.writerow(springBflLag)
    resultsWriter.writerow(snowEarlySpring)
    resultsWriter.writerow(snowEarlyWet)
    resultsWriter.writerow(snowSpringBfl)
    resultsWriter.writerow(snowSpringBflRate)
    resultsWriter.writerow(allOtherYearsRate)
    resultsWriter.writerow(rainWetSpring)
    resultsWriter.writerow(rainZeroFlow)
    resultsWriter.writerow(rainLateBfl)
    resultsWriter.writerow(rainEarlySpring)
    resultsWriter.writerow(rainLateWet)

header = ['class','wetInitCount','wetInitCount','springBflLag','snowEarlySpring','snowEarlyWet','snowSpringBfl','snowSpringBflRate','allOtherYearsRate',\
          'rainWetSpring','rainZeroFlow','rainLateBfl','rainEarlySpring','rainLateWet']

with open('resultsOutput.csv') as csv_file:
    resultsNoHeaderLists = []
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        resultsNoHeaderLists.append(row)
        
df = pd.DataFrame(resultsNoHeaderLists, index = header)

import pdb; pdb.set_trace()

#resultsNoHeader = []        
#for row, lists in enumerate(resultsNoHeaderLists):
#    import pdb; pdb.set_trace()
#    resultsNoHeader.append(None)
#    resultsNoHeader[row] = lists
    
    




