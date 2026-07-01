''' Create A Record of 15 person along with their name and salary.
display the name of person who are eligible for EWS category
if the salary is below 5 lakhs
'''

#--------------------------------------------------------------------------
#------------------Coding----------------------------------------------------

# creating list
names = []
salaries=[]

print("Enter the details of 15 person:")

# taking input from user
for x in range(15):
    name = input("Enter the name:")
    salary = int(input("Enter the salary:"))

    names.append(name)
    salaries.append(salary)


print("-----------------------------------------------------------------------")

#-------------------------------------------------------------------------------

# checking the eligibility for EWS category

print("The person who are eligible for EWS category are:")
for x in range(15):
    if (salaries[x] < 500000):
        print(names[x],end =",")

#-------------------------------------------------------------------------------

'''Output:
Enter the details of 15 person:
Enter the name:priya
Enter the salary:450000
Enter the name:garv
Enter the salary:40000
Enter the name:anmol
Enter the salary:420000
Enter the name:geeta
Enter the salary:650000
Enter the name:riya
Enter the salary:540000
Enter the name:rohit
Enter the salary:680000
Enter the name:renuka
Enter the salary:540000
Enter the name:krish
Enter the salary:65800 
Enter the name:manas
Enter the salary:540000
Enter the name:tia
Enter the salary:320000
Enter the name:shreya
Enter the salary:250000
Enter the name:aarushi
Enter the salary:450000
Enter the name:akansha
Enter the salary:560000
Enter the name:kritika
Enter the salary:258000
Enter the name:prachi
Enter the salary:120000
-----------------------------------------------------------------------
The person who are eligible for EWS category are:
priya,garv,anmol,krish,tia,shreya,aarushi,kritika,prachi,
'''
