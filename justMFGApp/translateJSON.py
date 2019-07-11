import json
import csv
import re

def strToInt(dict):
    '''
    If a dictionary value is numeric, it will be changed to an integer
    '''
    number_regex = re.compile(r"^\d*[.]?\d*$") #regular expression for a number or decimal number
    for entry in dict:
        if(isinstance(dict[entry], str)):
            if(number_regex.match(dict[entry]) and dict[entry] is not ''):
                dict[entry] = int(float(dict[entry])) #convert all numbers to integers
    return(dict)

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
            row = strToInt(row)
            data.append(row)

    with open(jsonFilePath, 'w') as jsonFile:
        jsonFile.write(json.dumps(data))



textFilePath = "MattG_TestFileforJSON.txt"
jsonFilePath = "Matt_G_TestFileforJSON.json"
