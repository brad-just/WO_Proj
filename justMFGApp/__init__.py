from flask import Flask
from justMFGApp.WorkOrders import WorkOrders
from justMFGApp.translateJSON import translateJSON

#Register the app
app = Flask(__name__)
app.secret_key = 'development key'
app.config['PRODUCTION_PDFS'] = "//SQL-ERP/ProjectEngineering/Production Drawings" #Input a valid path to pdfs

#Create a new WorkOrders object called data
Data = WorkOrders()

#Create new JSON
readPath = '/home/bradjust/WorkOrderApp/WO_Proj/justMFGApp/JSON/MattG_TestFileforJSON.txt'
writePath = '/home/bradjust/WorkOrderApp/WO_Proj/justMFGApp/JSON/MattG_TestFileforJSON.json'

header = ['WorkOrderNo', 'SoftWONo', 'TranNoRel', 'LineNo', 'QtyOrd', 'LineStatus', 'TranDate', 'PromiseDate', \
          'ItemID', 'Short Description','Hold', 'HoldReason','CustName', 'PrintedExpectShipRpt', 'QtyOnBO',\
          'QtyShip', 'QtyInvcd', 'QtyOpenToShip', 'OrderHold', 'OrderHoldReason']

translateJSON(readPath, writePath, head=header, sep=';')

#Extract data from JSON file
Data.setData(writePath) #input a valid path to a json file to be parsed

from justMFGApp import routes
