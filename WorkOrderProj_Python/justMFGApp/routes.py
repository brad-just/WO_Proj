from flask import render_template, url_for, request
from justMFGApp import app, Data
from operator import itemgetter
from datetime import datetime

#Function specifically designed convert a string to 0 for sorting purposes
#(i.e. strings will be inserted at the beginning)
def strToZero(dic, t):
    val = dic[t]
    if(isinstance(val,str)):
        val = 0
    return(val)

@app.route("/", methods=['POST', 'GET'])
@app.route("/index", methods=['POST', 'GET'])
def index():
    if(request.method=='POST'): #The user wants to sort the data on a specific key. The sort is done here
        if(Data.descending):
            Data.descending = False #Toggles accending sort and descending sort with the same button
        else:
            Data.descending = True
        for title in Data.header:
            if(title in request.form):
                if(title == 'Sales Order'):
                    Data.sort(criteria=lambda i: (strToZero(i,title), i[title])) #Because 'STOCK' appears in this field, we need to convert everything to a string before sorting
                else:
                    Data.sort(criteria=itemgetter(title)) #Sort dictionary by the title field
    return(render_template("index.html", orders=Data, datetime=datetime))


@app.route("/pdf")
def pdf():
    return(render_template("pdf.html", orders=Data))
