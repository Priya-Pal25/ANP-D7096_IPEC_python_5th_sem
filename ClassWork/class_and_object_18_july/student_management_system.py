'''-------------------------------- Problem 1: Student Management System-----------------------------
Problem Statement 
Create a class named Student to store and display a student's details. 
Requirements 
1. Create a class Student.  
2. Define the following instance variables:  
o student_id  
o name  
o course  
o marks  
3. Create a method accept_data() to take input from the user.  
4. Create a method display_data() to display all student details.  
5. Create another method check_result() that:  
o Displays "Pass" if marks are 35 or above  
o Displays "Fail" otherwise.  
6. Create an object of the class and call all the methods.  
Sample Input 
Enter Student ID : 101 
Enter Name : Rahul 
Enter Course : Python 
Enter Marks : 78 
Expected Output ------ Student Details ------ 
Student ID : 101 
Name       : Rahul 
Course     : Python 
Marks      : 78 
Result     : Pass 
-------------------------------------------------------------------------------------------------
'''

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------Coding-------------------------------------------

class student:
    def __init__(self):
        self.student_id = 0
        self.name = ""
        self.course = ""
        self.marks = 0

    def accept_data(self):
        self.student_id = int(input("Enter the Student ID : "))
        self.name = input("Enter the name : ")
        self.course = input("Enter the course name: ")
        self.marks = int(input("Enter the marks : "))

    def display_result(self):
        print("---------- Student details----------")
        print("Student ID : ",self.student_id)
        print("Name : ",self.name)
        print("Course : ",self.course)
        print("Marks : ",self.marks)

    def check_result(self):
        if (self.marks >= 35):
            print("Result : Pass")
        else:
            print("Result : Fail")

#-----------------------------------------------------------------------------------
#----------------------------------------main program-------------------------------
s1 = student()
s1.accept_data()
s1.display_result()
s1.check_result()

#-------------------------------------------------------------------------------------
'''Output :
Enter the Student ID : 201
Enter the name : Amit
Enter the course name: Btech
Enter the marks : 67
---------- Student details----------
Student ID :  201
Name :  Amit
Course :  Btech
Marks :  67
Result : Pass
'''
#-----------------------------------------------------------------------------------------