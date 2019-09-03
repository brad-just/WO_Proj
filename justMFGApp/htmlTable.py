import simplejson as json
import datetime
import pymssql

def myconverter(o):
    if isinstance(o, datetime.date):
        return o.__str__()

class Table(object):
    def __init__(self):
        self.data = [{}]
        self.header = [] #List representing the table headers

    def setDataFromJSONFile(self, json_path):
        with open(json_path, 'r') as read_file: #open the json dump file for reading
            self.data = json.load(read_file)
        if(self.data):
            self.header = header = list(self.data[0].keys())

    def setDataFromSQL(self, host, user, password, database, query):
        conn = pymssql.connect(host=host, user=user, password=password, database=database)
        cursor = conn.cursor(as_dict=True)

        cursor.execute(query)

        self.data = cursor.fetchall()
        if(self.data):
            self.header = [key for key in self.data[0]]

        cursor.close()
        conn.close()

    def SQLtoJSONFile(self, host, user, password, database, query, file):

        conn = pymssql.connect(host=host, user=user, password=password, database=database)
        cursor = conn.cursor(as_dict=True)

        cursor.execute(query)

        data = cursor.fetchall()
        self.header = [key for key in data[0]]

        cursor.close()
        conn.close()

        with open(file, 'w') as jsonFile:
            jsonFile.write(json.dumps(data, default=myconverter))

    def setDepartment(self, dept):
        self.department = dept.title()

    def filterJSONbyID(self, ItemID, file_path):

        new_data = []

        for line in self.data:
            if(line['ItemID'] == ItemID):
                new_data.append(line)

        with open(file_path, 'w') as write_file:
            write_file.write(json.dumps(new_data))
