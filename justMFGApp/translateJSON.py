import json
import csv
import re

def strToInt(string):
    '''
    If a string is a integer or decimal number it is converted to an int type
    '''
    number_regex = re.compile(r"^\d*[.]?\d*$") #regular expression for a number or decimal number
    if(isinstance(string, str)):
        if(number_regex.match(string) and string is not ''):
            string = int(float(string)) #convert all numbers to integers
    return(string)

def transformDate(string):
    '''
    If a string is a date then chop off the hours, minutes, and seconds
    '''
    if(isinstance(string,str)):
        if('00:00:00' in string):
            string = string[0:-9] #Chop off the 00:00:00
    return(string)


def conversions(dic_value):
    '''
    Transforms dictionary values if they meet certain criteria
    '''
    dic_value = strToInt(dic_value)
    dic_value = transformDate(dic_value)
    return(dic_value)

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
            for entry in row:
                row[entry] = conversions(row[entry])
            data.append(row)

    with open(jsonFilePath, 'w') as jsonFile:
        jsonFile.write(json.dumps(data))
