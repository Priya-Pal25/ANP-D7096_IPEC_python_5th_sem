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

#---------------------------------------------------------------------------------------------------------------

# Validating houses

if (house <= 0):
    exit("Number of houses must be positive")

#-------------------------------------------------------------------------------------------------------------------

total_units = 0
#Accept the monthly units consumed by each house.
for x in range(1,house+1):
    units = float(input("Enter the units consumed (monthly): "))

    # validating units

    if (units <= 0):
        exit("Units must be positive")

    #-------------------------------------------------------------------------------------------------------------------


    total_units = total_units + units
    #-------------------------------------------------------------------------------------------------------------------

    #  analyzing electricity consumption of N houses  

    if x == 1:
        highest = units
        lowest= units

    
    else:
        if (units > highest):
            highest = units
        if (units < lowest):
            lowest = units
        
    



# Calculate and display  Total units consumed 
print("Total unit Consumption : " ,total_units)

# Calculate and display Average units consumed  
print("Average unit Consumption :", (total_units/house))

# Calculate and display  Highest consumption
print("Highest Consumption :",highest)

# Calculate and display Lowest consumption 
print("Lowest Consumption : ",lowest)

#---------------------------------------------------------------------------------------------------------------------------------------

'''Output:
Enter the no of houses : 5
Enter the units consumed (monthly): 23
Enter the units consumed (monthly): 47
Enter the units consumed (monthly): 56
Enter the units consumed (monthly): 84
Enter the units consumed (monthly): 14
Total unit Consumption :  224.0
Average unit Consumption : 44.8
Highest Consumption : 84.0
Lowest Consumption :  14.0
'''


