'''' ------------------------------ Employee Information System ----------------------------------

Create a dictionary where: 
• Employee ID is the key.  
• Value is another dictionary containing:  
o Name  
o Department  
o Salary  
Perform the following operations: 
• Display all employee details.  
• Search for an employee using Employee ID.  
• Increase the salary of all employees by 10%.  
• Display employees belonging to a specific department entered by the user.  
-------------------------------------------------------------------------------------------------
'''

#-------------------------------------------------------------------------------------------------
#----------------------------------coding---------------------------------------------------------

# Create an empty dictionary
employees = {}

# Input employee details
n = int(input("Enter the number of employees: "))

for i in range(n):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    employees[emp_id] = {
        "Name": name,
        "Department": department,
        "Salary": salary
    }
print("------------------------------------------------------------------------------------")
#---------------------------------------------------------------------------------------

# Display all employee details
print("Employee Details:")
for emp_id in employees:
    print("Employee ID:", emp_id)
    print("Name:", employees[emp_id]["Name"])
    print("Department:", employees[emp_id]["Department"])
    print("Salary:", employees[emp_id]["Salary"])
print("----------------------------------------------------------------------")

#---------------------------------------------------------------------------------------

# Search for an employee using Employee ID
search_id = input("Enter Employee ID to search: ")

if search_id in employees:
    print("Employee Found")
    print("Name:", employees[search_id]["Name"])
    print("Department:", employees[search_id]["Department"])
    print("Salary:", employees[search_id]["Salary"])
else:
    print("Employee not found.")

print("-------------------------------------------------------------------------------")
#-------------------------------------------------------------------------------------------

# Increase salary by 10%
for emp_id in employees:
    employees[emp_id]["Salary"] = employees[emp_id]["Salary"] * 0.10

print("Employee Details after 10% Salary Increase:")
for emp_id in employees:
    print("Employee ID:", emp_id)
    print("Name:", employees[emp_id]["Name"])
    print("Department:", employees[emp_id]["Department"])
    print("Salary:", employees[emp_id]["Salary"])
print("-----------------------------------------------------------------------------")

#---------------------------------------------------------------------------

# Display employees of a specific department
dept = input("Enter Department to search: ")

print("Employees in", dept, "Department:")
found = False

for emp_id in employees:
    if employees[emp_id]["Department"] == dept:
        print("Employee ID:", emp_id)
        print("Name:", employees[emp_id]["Name"])
        print("Salary:", employees[emp_id]["Salary"])
        found = True

if found == False:
    print("No employees found in this department.")

#-----------------------------------------------------------------------------------------------
'''Output:
Enter the number of employees: 3
Enter Employee ID: 101
Enter Employee Name: jake
Enter Department: advertising
Enter Salary: 45000
Enter Employee ID: 201
Enter Employee Name: riya
Enter Department: marketing
Enter Salary: 45000
Enter Employee ID: 105
Enter Employee Name: himanshu
Enter Department: finance
Enter Salary: 50000
------------------------------------------------------------------------------------
Employee Details:
Employee ID: 101
Name: jake
Department: advertising
Salary: 45000.0
Employee ID: 201
Name: riya
Department: marketing
Salary: 45000.0
Employee ID: 105
Name: himanshu
Department: finance
Salary: 50000.0
----------------------------------------------------------------------
Enter Employee ID to search: 201
Employee Found
Name: riya
Department: marketing
Salary: 45000.0
-------------------------------------------------------------------------------
Employee Details after 10% Salary Increase:
Employee ID: 101
Name: jake
Department: advertising
Salary: 4500.0
Employee ID: 201
Name: riya
Department: marketing
Salary: 4500.0
Employee ID: 105
Name: himanshu
Department: finance
Salary: 5000.0
-----------------------------------------------------------------------------
Enter Department to search: finance
Employees in finance Department:
Employee ID: 105
Name: himanshu
Salary: 5000.0
'''