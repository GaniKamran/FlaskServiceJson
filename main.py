from flask import Flask, url_for, redirect, render_template, request,jsonify
from flask_restful import Api, Resource
from collections import*
import pyodbc
from ipaddress import*
import json
connection = pyodbc.connect('Driver={SQL Server};' 'Server=QENI\FG;' 'Database=DataPersonal;' 'Trusted_connection=yes;')
app = Flask(__name__)
api = Api(app)
@app.route("/adding")
def  RengersSlot():
    cursor = connection.cursor()
    data = cursor.execute('select *From PersonTable ')
    query_results = [dict(line) for line in [zip([column[0] for column in cursor.description], row) for row in cursor.fetchall()]]
    return jsonify(query_results)
@app.route("/<id>")
def SelectTable (id):
    cursor = connection.cursor()
    data = cursor.execute('select *From PersonTable where Id=?', id)
    query_results = [dict(line) for line in
                     [zip([column[0] for column in cursor.description], row) for row in cursor.fetchall()]]
    return jsonify(query_results)
@app.route("/delete/<id>")
def DeleteTable (id):
    cursor = connection.cursor()
    data = cursor.execute('Delete from PersonTable where Id=?', id)
    return redirect(url_for("RengersSlot"))
@app.route("/add/<dictionary>")
def addelements(AddElmts):
    cursor=connection.cursor()
    data = cursor.execute('Insert into PersonTable(Name, Surname,) values(?,?);',(AddElmts["Name"],AddElmts["Surname"]))
    return redirect(url_for("RengersSlot"))

class PersonList(Resource):
    def get(self,name):
        return names[name]
class PersonTask(Resource):
    def get(self):
        cursor = connection.cursor()
        data=cursor.execute('select *From PersonTable ')
        query_results=[dict(line) for line in [zip([column[0] for column in cursor.description], row) for row in cursor.fetchall()]]
        return query_results
api.add_resource(PersonList, "/personlist/<string:name>")
api.add_resource(PersonTask, "/persontask")
if __name__=="__main__":
    app.run(debug=True)

