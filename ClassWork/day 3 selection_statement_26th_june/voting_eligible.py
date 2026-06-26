'''------------------Voting eligible-----------------------
write a program to check a person is eligible for voting or not.
A person will be eligible if age is 18 or more
'''
#--------------------------------------------------------------------
#-----------------------Coding----------------------------------------

# Taking age from the user

age = int(input("Enter age (in years): "))

#validating age provided by user
if (age <= 0):
    exit("Age must be positive")

#-----------------------------------------------------------------------

# checking the eligibility for voting

if (age >= 18):
    print("Eligible for voting")
else:
    print("Not Eligible for voting")

#-------------------------------------------------------------------------

'''Output:
Enter age (in years): 23
Eligible for voting       
'''        