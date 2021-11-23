import requests
import pprint
Base="http://127.0.0.1:5000/"
response=requests.get(Base + "persontask")
print(response.json())
import pyodbc
connection = pyodbc.connect('Driver={SQL Server};' 'Server=QENI\FG;' 'Database=DataPersonal;' 'Trusted_connection=yes;')
cursor = connection.cursor()
data = cursor.execute('select *From PersonTable')
for i in data:
 print(i)