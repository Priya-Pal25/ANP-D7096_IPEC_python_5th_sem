'''----------------------------------------Electricity Bill Analysis----------------------------------------------------------------------- 

An electricity department wants to analyze electricity consumption of N houses. 
Accept the monthly units consumed by each house. 
---------------------------------------------------------------------------------------------------------------------------------
Calculate and display: 
• Total units consumed  
• Average units consumed  
• Highest consumption  
• Lowest consumption  
----------------------------------------------------------------------------------------------------------------------------
'''

#----------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------Coding-----------------------------------------------------------------

# Taking input from the user
house = int(input("Enter the no of houses : "))
total_units = 0
max = 0
min = 0

#-------------------------------------------------------------------------------------------------------------------

#Accept the monthly units consumed by each house.
for x in range(1,house+1):
    units = float(input("Enter the units consumed (monthly): "))
    total_units = total_units + units
    
    if (units > max):
        max = units
    
    else:
        min = units
    



# Calculate and display  Total units consumed 
print("Total unit Consumption : " ,total_units)

# Calculate and display Average units consumed  
print("Average unit Consumption :", (total_units/house))

# Calculate and display  Highest consumption
print("Highest Consumption :",max)

# Calculate and display Lowest consumption 
print("Lowest Consumption : ",min)

#---------------------------------------------------------------------------------------------------------------------------------------

'''Output:
Enter the no of houses : 3
Enter the units consumed (monthly): 56
Enter the units consumed (monthly): 41
Enter the units consumed (monthly): 21
Total unit Consumption :  118.0
Average unit Consumption : 39.333333333333336
Highest Consumption : 56.0
Lowest Consumption :  21.0
'''


