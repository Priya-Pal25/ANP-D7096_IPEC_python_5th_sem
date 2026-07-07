'''-------------------------------- Student Grade Calculator ----------------------------------------------------------
Write a Python program that defines a function calculate_grade(marks). 
The function should: 
• Accept marks (0-100) as a parameter.  
• Return the grade according to the following criteria:  
o 90 and above → A+  
o 75-89 → A  
o 60-74 → B  
o 40-59 → C  
o Below 40 → Fail  
The main program should: 
• Accept marks of 5 students.  
• Call the function for each student.  
• Display the marks and corresponding grade.  
'''

#------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------Coding----------------------------------------------------------------

# function to calculate student grade

def calculate_grade(marks):
    if (marks >= 90 ):
        return 'A+'
    elif (marks >= 75 and marks <= 89):
        return 'A'
    elif (marks >= 60 and marks <= 74):
        return 'B'
    elif (marks >= 40 and marks <= 59):
        return 'C'
    else:
        return 'Fail'

#---------------------------------------------------------------------------------------------------------------------------

# main program
# taking input from user
for i in range(5):
    mark = float(input("Enter marks of the student : "))
    grade = calculate_grade(mark)
    print("marks : ",mark)
    print("Grade : " ,grade)


print("----------------------------------------------------------------------------------------------------------------------")

#-----------------------------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------------------------
'''Output:
Enter marks of the student : 54
marks :  54.0
Grade :  C
Enter marks of the student : 69
marks :  69.0
Grade :  B
Enter marks of the student : 58
marks :  58.0
Grade :  C
Enter marks of the student : 36
marks :  36.0
Grade :  Fail
Enter marks of the student : 97
marks :  97.0
Grade :  A+
'''