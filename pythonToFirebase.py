import csv
from firebase import firebase

firebase = firebase.FirebaseApplication('https://lccscoursework-807da.firebaseio.com/',None)

globalTempYears = []
globalTempValues = []

def readInFile(globalTempYears,globalTempValues):
    with open("annual_temp_cleaned.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            globalTempYears.append(int(row[0]))
            globalTempValues.append(float(row[1]))
        print("Read in file successfually")
        return

readInFile(globalTempYears,globalTempValues)
print(globalTempValues)


# store the list in firebase using loop 
for x in range(len(globalTempValues)): 
    result = firebase.post('/globaltemps/', [globalTempYears[x],globalTempValues[x]])
    # returns key for inserted data
    print(result)

            


