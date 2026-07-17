# import mysql.connector
import mysql.connector
#-----------------------------------------------------------------------------
# to establish connection
dataconnection = mysql.connector.connect(host = 'localhost',
    user = 'root',
    password = 'Palpriya_2509@',
    database = 'studentmanagement'
    )
#-----------------------------------------------------------------------------
# to create the cursor
cursorobj = dataconnection.cursor()
#-----------------------------------------------------------------------------
sql_query = 'delete from student where stdid = %s'

stdid = input("Enter the stdid you want to delete: ")
#------------------------------------------------------------------------------

value = (stdid,)
#------------------------------------------------------------------------------
# to execute the query
cursorobj.execute(sql_query,value)

#------------------------------------------------------------------------------
# to commit the changes
dataconnection.commit()
#-------------------------------------------------------------------------------
# to check if the data is deleted or not

if (cursorobj.rowcount > 0):
    print("Data deleted successfully")
else:
    print("Unable to delete data")

#--------------------------------------------------------------------------------

# to close the cursor object
cursorobj.close()

#to close the connection object
cursorobj.close()
#---------------------------------------------------------------------------------