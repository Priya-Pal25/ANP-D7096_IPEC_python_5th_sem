'''------------------------- Loan Eligibility Check -------------------------------------------

A bank considers an applicant eligible for a personal loan only if their monthly salary is ₹30,000 or 
more. 
Write a Python program to accept the applicant's monthly salary and display whether they are 
eligible to apply for the loan. 
----------------------------------------------------------------------------------------------
Sample Input 1 
Enter your monthly salary: 45000 
---------------------------------------------------------------------------------------------
Sample Output 1 
Congratulations! You are eligible to apply for the loan. 
--------------------------------------------------------------------------------------------
Sample Input 2 
Enter your monthly salary: 22000 
---------------------------------------------------------------------------------------------
Sample Output 2 
Sorry! You are not eligible to apply for the loan
----------------------------------------------------------------------------------------------
'''

#--------------------------------------------------------------------------------------------
#-------------------------------Coding-------------------------------------------------------

# Taking monthly salary from the user

salary = float(input("Enter your monthly salary(in Rs): "))
# Validating salary
if (salary <=0):
    exit("Monthly salary must be positive")
#--------------------------------------------------------------------------------------------

# verifying eligiblity for the loan

if (salary >= 30000):
    print("Conngratulations! You are eligible to apply for thhe loan.")
else:
    print("Sorry! You are not eligible to apply for the loan.")

#------------------------------------------------------------------------------------------------

'''Output:
Enter your monthly salary(in Rs): 50000
Conngratulations! You are eligible to apply for thhe loan.
'''

