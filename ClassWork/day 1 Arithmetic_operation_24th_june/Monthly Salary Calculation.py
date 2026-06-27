'''Write a Python program to calculate the total monthly salary of an employee by adding the fixed salary 
and incentive amount. '''

# Taking input from user

Basic_Salary = float(input("Enter the Basic Salary: " ))
incentive = float(input("Enter the Incentive amount: " ))
#----------------------------------------------------------------------------------------------------
# Displaying the input to the user

print("Basic Salary : " ,Basic_Salary)
print("Incentive : " ,incentive)
#----------------------------------------------------------------------------------------------------
# Displaying Total salary to the user 

print("Total Salary :",(Basic_Salary + incentive))
#------------------------------------------------------------------------------------------------------

'''Output:
Enter the Basic Salary: 50000.0
Enter the Incentive amount: 25000.0
Basic Salary :  50000.0
Incentive :  25000.0
Total Salary : 75000.0
'''