''' ---------------------------------------Scholarship Eligibility------------------------------------------  

A university provides a scholarship only to students who score 90 or above. 
Write a Python program to accept a student's percentage and determine whether the student is eligible. 
• If percentage is 90 or above, display: 
Scholarship Approved 
• Otherwise display: 
Scholarship Not Approved 
-----------------------------------------------------------------------------------------------------------
Sample Input 
92 
----------------------------------------------------------------------------------------------------------
Sample Output 
Scholarship Approved
----------------------------------------------------------------------------------------------------------
'''

#----------------------------------------------------------------------------------------------------------
#-----------------------------Coding-----------------------------------------------------------------------

# Taking student percentage input from the user

percentage = float(input("Enter the Student percentage (out of 100): "))

#---------------------------------------------------------------------------------------------------------

# Validating student percentage

if (percentage <= 0):
    exit("Student Percentage must be positive")

#---------------------------------------------------------------------------------------------------------

# Checking whether the scholarship is approved or not

if (percentage >= 90):
    print("Scholarship Approved")
else:
    print("Scholarship Not Approved")

#---------------------------------------------------------------------------------------------------------

'''Output:
Enter the Student percentage (out of 100): 97
Scholarship Approved
'''