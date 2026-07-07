'''-----------------------------Dictionary Search System---------------------------------- 
Write a Python program that defines a function search_student(student_dict, roll_no). 
The function should: 
• Accept a dictionary where:  
o Key = Roll Number  
o Value = Student Name  
• Search for the given roll number.  
• Return the student name if found; otherwise return "Student Not Found".  
The main program should: 
• Create a dictionary of at least 5 students.  
• Accept a roll number from the user.  
• Display the search result.  
'''

#------------------------------------------------------------------------------------------------
#-------------------------------------Coding-----------------------------------------------------

# function to search a student from a dictionary
def search_student(student_dict,roll_no):
    if roll_no in student_dict:
        return student_dict[roll_no]
    else:
        return 'Student Not Found'
    
#-------------------------------------------------------------------------------------------------

# main program
student_dict={}

# Taking input from the user
for i in range(5):
    roll= int(input("Enter the roll no : "))
    name = input("Enter name : ")
    student_dict[roll] = name

print("Student dictionary : ", student_dict)
print("-----------------------------------------------------------------------------------------------------")

# taking rollno to search from user
roll_no = int(input("Enter the roll number to search : "))

# displaying the result
print("Student name is : ", search_student(student_dict,roll_no))

#-----------------------------------------------------------------------------------------------------

'''Output:
Enter the roll no : 25
Enter name : riya
Enter the roll no : 32
Enter name : priya
Enter the roll no : 45
Enter name : anmol
Enter the roll no : 21
Enter name : renuka
Enter the roll no : 11
Enter name : aarushi
Student dictionary :  {25: 'riya', 32: 'priya', 45: 'anmol', 21: 'renuka', 11: 'aarushi'}
-----------------------------------------------------------------------------------------------------
Enter the roll number to search : 32
Student name is :  priya
'''