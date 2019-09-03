from flask import Flask
from justMFGApp.WorkOrders import WorkOrders
from justMFGApp.htmlTable import Table
from justMFGApp.config import config

#Register the app
app = Flask(__name__)
app.secret_key = config['sec_key']

#Create a new WorkOrders object called data
WO_Data_Gen = WorkOrders()
WO_Data_BowlCust = WorkOrders()
Orders_With_ItemID = WorkOrders()
Inventory = Table()
MaterialItems = Table()

from justMFGApp import routes
