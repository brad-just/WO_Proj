import json
import pymssql

class WorkOrders(object):
    def __init__(self):
        self.data = [{}]
        self.header = [] #List representing the table headers
        self.department = ''
        self.descending = False #Initialized to false but will have no effect until the user sorts for the first time

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
        self.header = [key for key in self.data[0]]

        cursor.close()
        conn.close()

    def setDepartment(self, dept):
        self.department = dept.title()
