from flask import Blueprint, render_template, url_for, request, redirect, session
from justMFGApp import app, WO_Data_Gen, WO_Data_BowlCust, Orders_With_ItemID, Inventory, MaterialItems
from justMFGApp.config import config
from justMFGApp.forms import DepartmentForm
from justMFGApp.sql_queries import build_sql_query_gen, build_sql_query_bowlcust, replenishments_query, material_items_query

@app.route("/", methods=['POST', 'GET'])
@app.route("/app-router", methods=['POST', 'GET'])
def app_router():
    return(render_template("app-router.html"))

@app.route("/workOrders", methods=['POST', 'GET'])
def workOrders():
    if(session.get('logged_in')):

        WO_Data_Gen.setDataFromSQL(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                               query=build_sql_query_gen(WO_Data_Gen.department))
        #WO_Data_Gen.setDataFromJSONFile('/Users/bradjust/Projects/Just MFG Projects/WO_Proj_v3/justMFGApp/static/json/Custom.json')

        #Set the department
        WO_Data_Gen.setDepartment(session['department'])
        ItemID = ''
        long_description = ''
        short_description = ''
        index = 0

        if(request.method=='POST'):
            if('ItemID' in request.form):
                ItemID = request.form['ItemID']
                long_description = request.form['LongDesc']
                short_description = request.form['ShortDesc']
                index = int(request.form['index'])
                WorkOrderKey = int(request.form['WorkOrderKey'])
                Orders_With_ItemID.setDataFromSQL(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                                       query=build_sql_query_gen(WO_Data_Gen.department, ItemID=ItemID))
                MaterialItems.setDataFromSQL(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                                       query=material_items_query(WorkOrderKey))

            #    filtered_file = '/Users/bradjust/Projects/Just MFG Projects/WO_Proj_v3/justMFGApp/static/JSON/Custom_filtered.json'
            #    WO_Data_Gen.filterJSONbyID(ItemID=ItemID, file_path=filtered_file)
            #    Orders_With_ItemID.setDataFromJSONFile(filtered_file)

        return(render_template("workOrders.html", gen_orders=WO_Data_Gen, additional_orders=Orders_With_ItemID, MaterialItems=MaterialItems,
                                                  item_id=ItemID, long_description=long_description, short_description=short_description,
                                                  department=WO_Data_Gen.department, scrollToIndex=index))
    else:
        return(redirect(url_for('wo_login')))

@app.route("/Bowlcust", methods=['POST', 'GET'])
def BowlCust():

    WO_Data_BowlCust.setDataFromSQL(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                           query=build_sql_query_bowlcust(WO_Data_BowlCust.department))
    #WO_Data_BowlCust.setDataFromJSONFile('/Users/bradjust/Projects/Just MFG Projects/WO_Proj_v3/justMFGApp/static/json/Bowlcust.json')

    #Set the department
    WO_Data_BowlCust.setDepartment('BowlCust')
    ItemID = ''
    long_description = ''
    short_description = ''
    index = 0

    if(request.method=='POST'):
        if('ItemID' in request.form):
            ItemID = request.form['ItemID']
            long_description = request.form['LongDesc']
            short_description = request.form['ShortDesc']
            index = int(request.form['index'])
            WorkOrderKey = int(request.form['WorkOrderKey'])

            Orders_With_ItemID.setDataFromSQL(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                                       query=build_sql_query_bowlcust(WO_Data_BowlCust.department, ItemID=ItemID))
            MaterialItems.setDataFromSQL(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                                   query=material_items_query(WorkOrderKey))

            #filtered_file = '/Users/bradjust/Projects/Just MFG Projects/WO_Proj_v3/justMFGApp/static/JSON/Bowlcust_filtered.json'
            #WO_Data_BowlCust.filterJSONbyID(ItemID=ItemID, file_path=filtered_file)
            #Orders_With_ItemID.setDataFromJSONFile(filtered_file)

    return(render_template("Bowlcust.html", bowlcust_orders=WO_Data_BowlCust, additional_orders=Orders_With_ItemID, MaterialItems=MaterialItems,
                                            item_id=ItemID, long_description=long_description, short_description=short_description,
                                            department=WO_Data_BowlCust.department, scrollToIndex=index))


@app.route("/wo_login", methods=['POST', 'GET'])
def wo_login():
    if(session.get('logged_in')):
        WO_Data_Gen.setDepartment(session['department']) #the session variable holds the cookies stored by the app
        WO_Data_BowlCust.setDepartment('BowlCust')
        return(redirect(url_for('workOrders')))
    else:
        form = DepartmentForm()
        if(request.method=='POST'):
            if(request.form['department'] != ''):
                session['logged_in'] = True
                session['department'] = request.form['department'].title()
                WO_Data_Gen.setDepartment(request.form['department'].title())
                WO_Data_BowlCust.setDepartment('BowlCust')
                return(redirect(url_for('workOrders')))
    return(render_template("wo_login.html", department=WO_Data_Gen.department, form=form))

@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['department'] = ''
    WO_Data_Gen.setDepartment('')
    WO_Data_BowlCust.setDepartment('')
    return(redirect(url_for('wo_login')))

pdfs = Blueprint("pdfs", __name__, static_url_path='/pdfs', static_folder='/pdfs')
app.register_blueprint(pdfs)

@app.route("/inventory", methods=['POST', 'GET'])
def inventory():
    Inventory.setDataFromSQL(host=config['sql_host'], user=config['sql_user'], password=config['sql_password'], database=config['sql_db'], \
                             query=replenishments_query())
    return(render_template("inventory.html", Inventory=Inventory))
