'''---------------------------------- Student Marks Management------------------------------------------------------------------- 

Create a dictionary to store the marks of 5 students, where the key is the student's name and the 
value is their marks. 
Perform the following operations: 
• Display all student names and marks.  
• Add a new student with marks.  
• Update the marks of an existing student.  
• Delete a student by name.  
• Display the student who scored the highest marks.  
-------------------------------------------------------------------------------------------------------------------------------------'''

#--------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------Coding-------------------------------------------------------------------------

# creating new dictionary
students = {}

for i in range(5):
    name = input("Enter the name of the student : ")
    marks = float(input("Enter the marks of the student : "))
    students[name] = marks

print("Dictionary is ")
print(students)

print("--------------------------------------------------------------------------------------------------")

# Displaying all student names and marks
for n,m in students.items():
    print(n,':',m)

#---------------------------------------------------------------------------------
# Add a new student with marks
 
print("---------------------------------------------------------------------------------------------")
print("Adding new student record")
new_name = input("Enter new student name: ")
new_marks = float(input("Enter marks : "))
students[new_name] = new_marks

print("After adding new student record")
print(students)
print("--------------------------------------------------------------------------------------------")
#----------------------------------------------------------------------------------

# Update the marks of an existing student

print("For Updating the marks of an existiong student ")
update_name = input("Enter updated name of the student : ")
if update_name in students:
    new_marks = float(input("Enter the marks : "))
    students[update_name] = new_marks
    print("updaation done successfully")

else:
    print("No such name in student")

print("Updated students ")
print(students)
print("-----------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------

# Delete a student by name

name = input("Enter student name to delete: ")
if name in students:
    del students[name]
    print("Student deleted successfully.")
else:
    print("Student not found.")

print("After deletion the dictionary is")
print(students)
print("----------------------------------------------------------------------------------")

#------------------------------------------------------------------------------------------
# Display the student who scored the highest marks

highest_student = max(students, key=students.get)
print("Student with Highest Marks:")
print(highest_student, ":", students[highest_student])

#-----------------------------------------------------------------------------------------
'''Output:
Enter the name of the student : Ankit
Enter the marks of the student : 58
Enter the name of the student : aman
Enter the marks of the student : 78
Enter the name of the student : jake
Enter the marks of the student : 88
Enter the name of the student : krish
Enter the marks of the student : 74
Enter the name of the student : riya
Enter the marks of the student : 92
Dictionary is 
{'Ankit': 58.0, 'aman': 78.0, 'jake': 88.0, 'krish': 74.0, 'riya': 92.0}
----------------------------------------------------------------------------
Ankit : 58.0
aman : 78.0
jake : 88.0
krish : 74.0
riya : 92.0
-------------------------------------------------------------------------------
Adding new student record
Enter new student name: manisha
Enter marks : 89
After adding new student record
{'Ankit': 58.0, 'aman': 78.0, 'jake': 88.0, 'krish': 74.0, 'riya': 92.0, 'manisha': 89.0}
-----------------------------------------------------------------------------------------
For Updating the marks of an existiong student 
Enter updated name of the student : jake
Enter the marks : 85
updaation done successfully
Updated students 
{'Ankit': 58.0, 'aman': 78.0, 'jake': 85.0, 'krish': 74.0, 'riya': 92.0, 'manisha': 89.0}
----------------------------------------------------------------------------------------
Enter student name to delete: krish
Student deleted successfully.
After deletion the dictionary is
{'Ankit': 58.0, 'aman': 78.0, 'jake': 85.0, 'riya': 92.0, 'manisha': 89.0}
-------------------------------------------------------------------------
Student with Highest Marks:
riya : 92.0
'''