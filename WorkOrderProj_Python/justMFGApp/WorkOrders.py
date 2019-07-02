import json

class WorkOrders(object):
    def __init__(self):
        self.data = [{}]
        self.header = [] #List representing the table headers
        self.department = ''
        self.descending = False #Initialized to false but will have no effect until the user sorts for the first time

    def setData(self, json_path):
        with open(json_path, 'r') as read_file: #open the json dump file for reading
            self.data = json.load(read_file)
        if(self.data):
            self.header = header = list(self.data[0].keys())

    def setDepartment(self, dept):
        self.department = dept.title()

    def sort(self, criteria):
        self.data = sorted(self.data, key=criteria, reverse=self.descending)
