'''---------------------------Electricity Consumption Category (if...elif...else Statement)-------------------------------------------------- 

An electricity department categorizes households based on monthly electricity consumption. 
• Up to 100 units → Low Consumption  
• 101-300 units → Moderate Consumption  
• Above 300 units → High Consumption  
Write a Python program to display the consumption category. 
---------------------------------------------------------------------------------------------------------------------------------------------
Sample Input 
245 
---------------------------------------------------------------------------------------------------------------------------------------------
Sample Output 
Moderate Consumption 
-------------------------------------------------------------------------------------------------------------------------------------------
'''

#------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------Coding------------------------------------------------------------------------------

# Taking electricity consumption input from the user

electricity_consumption = int(input("Enter Electricity Consumption (in units): "))

print("--------------------------------------------------------------------------------------------------------------------------------")

#---------------------------------------------------------------------------------------------------------------------------------------

# validating electricity consumption

if (electricity_consumption <= 0):
    exit("Invalid Input! Electricity Consumption must be poistive")

#-----------------------------------------------------------------------------------------------------------------------------------------

# checking and display the consumption category. 
if (electricity_consumption <= 100):
    print("Low Consumption")
elif (electricity_consumption >= 101 and electricity_consumption <= 300):
    print("Moderate Consumption")
else:
    print("High Consumption")

#-----------------------------------------------------------------------------------------------------------------------------------------

'''Output:
Enter Electricity Consumption (in units): 200
--------------------------------------------------------------------------------------------------------------------------------
Moderate Consumption
'''