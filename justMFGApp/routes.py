from flask import Blueprint, render_template, url_for, request, redirect, session
from justMFGApp import app, WO_Data
from justMFGApp.config import config
from justMFGApp.forms import DepartmentForm
from justMFGApp.sql_queries import build_sql_query

@app.route("/", methods=['POST', 'GET'])
@app.route("/index", methods=['POST', 'GET'])
def index():
    if(session.get('logged_in')):

        #Set the department
        WO_Data.setDepartment(session['department'])

        #Set the data on the page with a fresh sql query each time the page is entered, sort if a form was sumbitted by the page
        if(request.method=='POST'): #The user wants to sort the data on a specific key. The sort is done here
            if(WO_Data.descending):
                WO_Data.descending = False #Toggles accending sort and descending sort with the same button
            else:
                WO_Data.descending = True
            WO_Data.setDataFromSQL(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                                   query=build_sql_query(WO_Data.department, field=request.form['key'], sort_dir=WO_Data.descending))
        else:
            WO_Data.setDataFromSQL(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                                   query=build_sql_query(WO_Data.department))
        return(render_template("index.html", orders=WO_Data))
    else:
        return(redirect(url_for('login')))

@app.route("/login", methods=['POST', 'GET'])
def login():
    if(session.get('logged_in')):
        WO_Data.setDepartment(session['department']) #the session variable holds the cookies stored by the app
        return(redirect(url_for('index')))
    else:
        form = DepartmentForm()
        if(request.method=='POST'):
            if(request.form['department'] != ''):
                session['logged_in'] = True
                session['department'] = request.form['department'].title()
                WO_Data.setDepartment(request.form['department'].title())
                return(redirect(url_for('index')))
    return(render_template("login.html", orders=WO_Data, form=form))

@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['department'] = ''
    WO_Data.setDepartment('')
    return(redirect(url_for('login')))

pdfs = Blueprint('pdfs', __name__, static_url_path='/pdfs', static_folder='/pdfs')
app.register_blueprint(pdfs)
