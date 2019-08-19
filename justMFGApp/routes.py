from flask import Blueprint, render_template, url_for, request, redirect, session
from justMFGApp import app, WO_Data_Gen, WO_Data_BowlCust
from justMFGApp.config import config
from justMFGApp.forms import DepartmentForm
from justMFGApp.sql_queries import build_sql_query_gen, build_sql_query_bowlcust

@app.route("/", methods=['POST', 'GET'])
@app.route("/index", methods=['POST', 'GET'])
def index():
    if(session.get('logged_in')):

        #Set the department
        WO_Data_Gen.setDepartment(session['department'])
        WO_Data_BowlCust.setDepartment(session['department'])

        #Set the data on the page with a fresh sql query each time the page is entered, sort if a form was sumbitted by the page
        if(request.method=='POST'): #The user wants to sort the data on a specific key. The sort is done here
            if('top_key' in request.form):
                if(WO_Data_BowlCust.descending):
                    WO_Data_BowlCust.descending = False #Toggles accending sort and descending sort with the same button
                else:
                    WO_Data_BowlCust.descending = True
                WO_Data_BowlCust.setDataFromSQL(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                                       query=build_sql_query_bowlcust(WO_Data_BowlCust.department, field=request.form['top_key'], sort_dir=WO_Data_BowlCust.descending))
            else:
                if(WO_Data_Gen.descending):
                    WO_Data_Gen.descending = False #Toggles accending sort and descending sort with the same button
                else:
                    WO_Data_Gen.descending = True
                WO_Data_Gen.setDataFromSQL(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                                       query=build_sql_query_gen(WO_Data_Gen.department, field=request.form['bottom_key'], sort_dir=WO_Data_Gen.descending))

        else:
            WO_Data_Gen.setDataFromSQL(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                                   query=build_sql_query_gen(WO_Data_Gen.department))
            WO_Data_BowlCust.setDataFromSQL(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                                   query=build_sql_query_bowlcust(WO_Data_BowlCust.department))
        return(render_template("index.html", gen_orders=WO_Data_Gen, bowlcust_orders=WO_Data_BowlCust))
    else:
        return(redirect(url_for('login')))

@app.route("/login", methods=['POST', 'GET'])
def login():
    if(session.get('logged_in')):
        WO_Data_Gen.setDepartment(session['department']) #the session variable holds the cookies stored by the app
        WO_Data_BowlCust.setDepartment(session['department'])
        return(redirect(url_for('index')))
    else:
        form = DepartmentForm()
        if(request.method=='POST'):
            if(request.form['department'] != ''):
                session['logged_in'] = True
                session['department'] = request.form['department'].title()
                WO_Data_Gen.setDepartment(request.form['department'].title())
                WO_Data_BowlCust.setDepartment(request.form['department'].title())
                return(redirect(url_for('index')))
    return(render_template("login.html", gen_orders=WO_Data_Gen, form=form))

@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['department'] = ''
    WO_Data_Gen.setDepartment('')
    return(redirect(url_for('login')))

pdfs = Blueprint('pdfs', __name__, static_url_path='/pdfs', static_folder='/pdfs')
app.register_blueprint(pdfs)
