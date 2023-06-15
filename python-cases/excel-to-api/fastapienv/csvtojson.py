import csv, json

csvFilePath = "records.csv"
jsonFilePath = "updated.json"

#reading csv and adding data to dictionary
data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        EmpID = csvRow['EmpID']
        data[EmpID] = csvRow

#write to json file
with open('jsonFilePath', 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))