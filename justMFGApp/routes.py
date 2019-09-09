from flask import Blueprint, render_template, url_for, request, redirect, session
import json
from justMFGApp import app, Custom, Bowl, BowlCust, Laser, Brake, Inventory, Engineering
from justMFGApp.config import config
from justMFGApp.forms import DepartmentForm
from justMFGApp.sql_queries import build_sql_query_gen, build_sql_query_bowlcust, replenishments_query, material_items_query, get_orders_by_operation

@app.route("/", methods=['POST', 'GET'])
@app.route("/app-router", methods=['POST', 'GET'])
def app_router():
    if(session.get('pin_entered')):
        return(render_template("app-router.html", title='JMFG App', header_link='app_router', department='Just MFG', pin=True))
    elif(request.method=='POST'):
        print(request.form)
        if('pin' in request.form):
            with open('/Users/bradjust/Projects/Just MFG Projects/WO_Proj_v4/justMFGApp/static/JSON/pin.json') as read_file:
                correct_pin = json.load(read_file)['pin']
            if(request.form['pin']==correct_pin):
                session['pin_entered'] = True
                return(redirect(url_for( "app_router" )))
    return(render_template("app-router.html", title='JMFG App', header_link='app_router', department='Just MFG', pin=False))

@app.route("/laser", methods=['POST', 'GET'])
def laser():
    index = 0
    Steps = False

    Laser.setDataFromSQL(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                        query=get_orders_by_operation('LASER'))

    if(request.method=='POST'):
        if('WorkOrderKey' in request.form):
            index = int(request.form['index'])
            WorkOrderKey = int(request.form['WorkOrderKey'])
            Steps = Laser.executeQuery(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                                        query=material_items_query(WorkOrderKey))
    return(render_template('laser.html', title='Laser', header_link='laser', department='Laser', Orders=Laser, Steps=Steps, scrollToIndex=index, ItemID_link='laser'))

@app.route("/brake", methods=['POST', 'GET'])
def brake_press():
    index = 0
    Steps = False

    Brake.setDataFromSQL(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                        query=get_orders_by_operation('BRAKE'))

    if(request.method=='POST'):
        if('WorkOrderKey' in request.form):
            index = int(request.form['index'])
            WorkOrderKey = int(request.form['WorkOrderKey'])
            Steps = Brake.executeQuery(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                                        query=material_items_query(WorkOrderKey))

    return(render_template('brake-press.html', title='Brake Press', header_link='brake_press', department='Brake Press', Orders=Brake, Steps=Steps, scrollToIndex=index, ItemID_link='brake_press'))

@app.route("/workOrders", methods=['POST', 'GET'])
def workOrders():
    if(session.get('pin_entered')):
        if(session.get('logged_in')):

            index = 0
            Steps = False

            if(session['department'] == 'Custom'):
                Custom.setDataFromSQL(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                                       query=build_sql_query_gen(session['department']))

                if(request.method=='POST'):
                    print(request)
                    if('WorkOrderKey' in request.form):
                        index = int(request.form['index'])
                        WorkOrderKey = int(request.form['WorkOrderKey'])
                        Steps = Custom.executeQuery(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                                                    query=material_items_query(WorkOrderKey))

                return(render_template("workOrders.html", title='Custom', Orders=Custom, Steps=Steps, department=session['department'], scrollToIndex=index, ItemID_link='workOrders'))
            elif(session['department'] == 'Bowl'):
                Bowl.setDataFromSQL(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                                       query=build_sql_query_gen(session['department']))

                if(request.method=='POST'):
                    if('WorkOrderKey' in request.form):
                        index = int(request.form['index'])
                        WorkOrderKey = int(request.form['WorkOrderKey'])
                        Steps = Bowl.executeQuery(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                                                    query=material_items_query(WorkOrderKey))

                return(render_template("workOrders.html", title='Bowl', Orders=Bowl, Steps=Steps, department=session['department'], scrollToIndex=index, ItemID_link='workOrders'))
            else:
                Engineering.setDataFromSQL(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                                       query=build_sql_query_gen(session['department']))

                if(request.method=='POST'):
                    if('WorkOrderKey' in request.form):
                        index = int(request.form['index'])
                        WorkOrderKey = int(request.form['WorkOrderKey'])
                        Steps = Engineering.executeQuery(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                                                    query=material_items_query(WorkOrderKey))

                return(render_template("workOrders.html", title='Engineering', Orders=Engineering, Steps=Steps, department=session['department'], scrollToIndex=index, ItemID_link='workOrders'))
        else:
            return(redirect(url_for('wo_login')))
    else:
        return(redirect(url_for( 'app_router' )))

@app.route("/Bowlcust", methods=['POST', 'GET'])
def Bowlcust():
    if(session.get('pin_entered')):
        BowlCust.setDataFromSQL(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                               query=build_sql_query_bowlcust())

        index = 0
        Steps = False

        if(request.method=='POST'):
            if('WorkOrderKey' in request.form):
                index = int(request.form['index'])
                WorkOrderKey = int(request.form['WorkOrderKey'])

                Steps = BowlCust.executeQuery(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                                                query=material_items_query(WorkOrderKey))

        return(render_template("Bowlcust.html", title='BowlCust', Orders=BowlCust, Steps=Steps, department='BowlCust', scrollToIndex=index, ItemID_link='Bowlcust'))
    else:
        return(redirect(url_for( 'app_router' )))

@app.route("/inventory", methods=['POST', 'GET'])
def inventory():
    if(session.get('pin_entered')):
        Inventory.setDataFromSQL(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                                 query=replenishments_query())
        return(render_template("inventory.html", title='Inventory', Inventory=Inventory))
    else:
        return(redirect(url_for( 'app_router' )))

@app.route("/wo-login", methods=['POST', 'GET'])
def wo_login():
    if(session.get('pin_entered')):
        if(session.get('logged_in')):
            return(redirect(url_for('workOrders')))
        else:
            form = DepartmentForm()
            if(request.method=='POST'):
                if(request.form['department'] != ''):
                    session['logged_in'] = True
                    session['department'] = request.form['department'].title()
                    return(redirect(url_for('workOrders')))
        return(render_template("wo-login.html", title='Choose Department', department='', form=form))
    else:
        return(redirect(url_for( 'app_router' )))

@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['department'] = ''
    return(redirect(url_for('wo_login')))

pdfs = Blueprint("pdfs", __name__, static_url_path='/pdfs', static_folder='/pdfs')
app.register_blueprint(pdfs)
