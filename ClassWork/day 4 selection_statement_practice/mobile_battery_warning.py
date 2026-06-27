'''----------------------------------- Mobile Battery Warning ------------------------------------------------

A smartphone displays a low battery warning only when the battery percentage falls below 15%. 
Write a Python program to accept the battery percentage. 
If the battery is below 15, display: 
Connect Charger Immediately 
Otherwise, display nothing. 
-------------------------------------------------------------------------------------------------------------
Sample Input 
10 
-------------------------------------------------------------------------------------------------------------
Sample Output 
Connect Charger Immediately
-------------------------------------------------------------------------------------------------------------
'''
#------------------------------------------------------------------------------------------------------------
#-------------------------------------------Coding-----------------------------------------------------------

# Taking battery percentage input from the user

battery_percentage = float(input("Enter the Battery Percentage : "))

print("------------------------------------------------------------------------------------------------------")

#-------------------------------------------------------------------------------------------------------------

# Validating battery percentage

if (battery_percentage < 0 or battery_percentage >100):
    exit("Invalid data")

#------------------------------------------------------------------------------------------------------------------

# Checking battery percentage and displaying battery warning

if (battery_percentage < 15):
    print("Connect Charger Immediately")



#----------------------------------------------------------------------------------------------------------------

'''Output:
Enter the Battery Percentage : 10
------------------------------------------------------------------------------------------------------
Connect Charger Immediately
'''