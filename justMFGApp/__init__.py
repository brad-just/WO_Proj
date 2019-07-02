from flask import Flask
from justMFGApp.WorkOrders import WorkOrders

#Register the app
app = Flask(__name__)
app.secret_key = 'development key'

#Create a new WorkOrders object called data
Data = WorkOrders()

#Extract data from JSON file
Data.setData('/Users/bradjust/desktop/projects/Just MFG Projects/WorkOrderProj_Python/justMFGApp/JSON/WorkOrderView1.json') #input a valid path to a json file to be parsed

from justMFGApp import routes
