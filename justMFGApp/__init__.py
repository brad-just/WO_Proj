from flask import Flask
from justMFGApp.WorkOrders import WorkOrders

#Register the app
app = Flask(__name__)
app.secret_key = 'development key'
app.config['PRODUCTION_PDFS'] = "//SQL-ERP/ProjectEngineering/Production Drawings" #For serving production drawing pdfs

#Create a new WorkOrders object called data
Data = WorkOrders()

#Extract data from JSON file
Data.setData('/home/bradjust/WorkOrderApp/WO_Proj/justMFGApp/JSON/WorkOrderView1.json') #input a valid path to a json file to be parsed

from justMFGApp import routes
