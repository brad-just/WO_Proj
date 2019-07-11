import json
import csv

def translateJSON(readPath, writePath, head=None, sep=',' ):
    '''
    Function to tranlate a text file into JSON
    '''

    textFilePath = readPath
    jsonFilePath = writePath
    data = []

    with open(textFilePath) as textFile:
        reader = csv.DictReader(textFile, delimiter=sep, fieldnames=head)
        if(head):
            next(reader)
        for row in reader:
            data.append(row)

    with open(jsonFilePath, 'w') as jsonFile:
        jsonFile.write(json.dumps(data))



textFilePath = "MattG_TestFileforJSON.txt"
jsonFilePath = "Matt_G_TestFileforJSON.json"
