'''----------------------------------------------Employee Salary Statistics---------------------------------------------------------- 

A company has N employees. 
Accept the salary of each employee and determine: 
• Highest salary  
• Lowest salary  
• Average salary  
• Number of employees earning more than ₹50,000  
-------------------------------------------------------------------------------------------------------------------------------------
'''

#-----------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------Coding-------------------------------------------------------------------------

# Taking input from the user
emp = int (input("Enter the no of Employees : "))

#---------------------------------------------------------------------------------------------------------------

# Validating salary

if (emp <= 0):
    exit("Number of employees must be positive")

#-------------------------------------------------------------------------------------------------------------------

total_Salary = 0
count = 0

# Accepting the salary of each employee 
for x in range(1,emp+1):
    salary = float(input("Enter the salary : "))

    # validating units

    if (salary <= 0):
        exit("Employee salary must be positive")

    #-------------------------------------------------------------------------------------------------------------------

    # Calulating total salary
    total_Salary = total_Salary + salary

    #------------------------------------------------------------------------------------------------------------------
    #  analyzing salary of N employee 

    if x == 1:
        highest = salary
        lowest= salary

    
    else:
        if (salary > highest):
            highest = salary
        if (salary < lowest):
            lowest = salary
        
    if (salary > 50000):
        count = count +1


#-------------------------------------------------------------------------------------------------------------------

# Calculate and display Average salary
print("Average unit Consumption :", (total_Salary/emp))

# Calculate and display  Highest salary
print("Highest Consumption :",highest)

# Calculate and display Lowest salary
print("Lowest Consumption : ",lowest)

# Calculate and display the no of employees earning more than ₹50,000
print("Number of employees earning more than 50000 : ",count)
#-------------------------------------------------------------------------------------------------------------------------

'''Output:
Enter the no of Employees : 5
Enter the salary : 25000
Enter the salary : 50000
Enter the salary : 75000
Enter the salary : 14000
Enter the salary : 65000
Average unit Consumption : 45800.0
Highest Consumption : 75000.0
Lowest Consumption :  14000.0
'''
