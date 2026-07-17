#to import mysql.connector module
import mysql.connector
#------------------------------------------------------------
#to establish connection with mysql
dataconnection = mysql.connector.connect(host = 'localhost',
	user = 'root',
	password = 'Palpriya_2509@',
	database = 'studentmanagement'
	)
#------------------------------------------------------------
# to create a cursor object
cursorobj = dataconnection.cursor()
#------------------------------------------------------------
# writing insert query
sql_query = 'insert into student values (%s,%s,%s,%s)'

#------------------------------------------------------------
stdid ='std106'
stdname = 'Divya'
standard = '12th'
age = 18
#put the values to be inserted inside a tuple
values = (stdid,stdname,standard,age)
#------------------------------------------------------------
#to execute the query
cursorobj.execute(sql_query , values)
#------------------------------------------------------------
#to commit changes
dataconnection.commit()
#------------------------------------------------------------
#to check data inserted or not
if(cursorobj.rowcount  > 0):
	print("Data inserted successfully")
else:
	print("Unable to insert data")
#------------------------------------------------------------
#to close cursur object
cursorobj.close()
#to close connection object
dataconnection.close()
#------------------------------------------------------------
