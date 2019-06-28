from flask import Flask
from justMFGApp.WorkOrders import WorkOrders

#Register the app
app = Flask(__name__)

#Create a new WorkOrders object called data
Data = WorkOrders()

#Extract data from JSON file
Data.setData('PATH_TO_JSON') #input a valid path to a json file to be parsed
Data.setDepartment("DEPARTMENT") #input the department to be displayed

from justMFGApp import routes
