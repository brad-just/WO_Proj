from flask import render_template, url_for, request, redirect, session, send_from_directory
from justMFGApp import app, Data
from justMFGApp.forms import DepartmentForm
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
    if(session.get('logged_in')):
        Data.setDepartment(session['department'])
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
    else:
        return(redirect(url_for('login')))

@app.route("/login", methods=['POST', 'GET'])
def login():
    if(session.get('logged_in')):
        Data.setDepartment(session['department']) #the session variable holds the cookies stored by the app
        return(redirect(url_for('index')))
    else:
        form = DepartmentForm()
        if(request.method=='POST'):
            if(request.form['department'] != ''):
                session['logged_in'] = True
                session['department'] = request.form['department'].title()
                Data.setDepartment(request.form['department'].title())
                return(redirect(url_for('index')))
    return(render_template("login.html", orders=Data, form=form))

@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['department'] = ''
    Data.setDepartment('')
    return(redirect(url_for('login')))

@app.route("/SQL-ERP/ProjectEngineering/Production Drawings/<path:filename>")
def productionPDFs(filename):
    return(send_from_directory(app.config['PRODUCTION_PDFS'], filename))
