from flask import Flask
from justMFGApp.WorkOrders import WorkOrders
from justMFGApp.config import config

#Register the app
app = Flask(__name__)
app.secret_key = config['sec_key']

#Create a new WorkOrders object called data
WO_Data = WorkOrders()

from justMFGApp import routes
