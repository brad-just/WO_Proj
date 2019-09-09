from flask import Flask
from justMFGApp.htmlTable import Table
from justMFGApp.config import config

#Register the app
app = Flask(__name__)
app.secret_key = config['sec_key']

#Create Table objects wich will house the table data for each page
Custom = Table()
Bowl = Table()
BowlCust = Table()
Engineering = Table()
Laser = Table()
Brake = Table()
Inventory = Table()

from justMFGApp import routes
