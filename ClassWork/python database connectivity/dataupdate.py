# to import mysql.connector
import mysql.connector
#-------------------------------------------------------------------------
dataconnection = mysql.connector.connect(host = 'localhost',
    user = 'root',
    password = 'Palpriya_2509@',
    database = 'studentmanagement')

#-------------------------------------------------------------------------
# to create a cursor object 
cursorobj = dataconnection.cursor()
#------------------------------------------------------------------------
# writing sql query
sql_query = 'update student set standard = %s ,age = %s where stdid = %s'
#--------------------------------------------------------------------------
stdid = input("Enter the stdid you want to update : ")
standard = input("Enter the standard:")
age = int(input("Enter the age : "))

values = (standard ,age ,stdid)
#---------------------------------------------------------------------------
# to execute query
cursorobj.execute(sql_query,values)
#---------------------------------------------------------------------------
# to commit the changes
dataconnection.commit()
#---------------------------------------------------------------------------
# to check if the data is updated or not
if (cursorobj.rowcount > 0):
    print("Data updated successfully")
else:
    print("Unable to update")

#----------------------------------------------------------------------------
# to close the cursor object
cursorobj.close()
# to close the connection
dataconnection.close()
#-----------------------------------------------------------------------------
