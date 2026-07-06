'''-------------------------------Student Subject Report Card------------------------------------  

Create a nested dictionary to store marks of students in three subjects. 
Example:
{ 
'Rahul': {'Math': 85, 'Science': 90, 'English': 88}, 
'Priya': {'Math': 78, 'Science': 95, 'English': 82}, 
'Ankit': {'Math': 91, 'Science': 89, 'English': 94} 
} 
Write a program to: 
• Calculate the total marks of each student.  
• Calculate the average marks of each student.  
• Display the topper based on total marks.  
• Display the subject-wise highest marks along with the student's name.  
• Display students whose average is greater than or equal to 85.
-------------------------------------------------------------------------------------------------
'''

#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------Coding------------------------------------------------------------

# creating nested dictionary

students = {'Aman' : {'Math':87 ,'Science':78,'English': 92},'Jake' : {'Math' : 87 , 'Science': 76 , 'English':91},
'Ankit' : {'Math': 85, 'Science' : 83, 'English' : 93}}

#--------------------------------------------------------------------------------------------------------------

# total and average marks of each student

totals = {}

for student, marks in students.items():
    total = sum(marks.values())
    average = total / len(marks)
    totals[student] = total

    print(student)
    print("Total Marks =", total)
    print("Average Marks =", average)
print("---------------------------------------------------------------------------------------------------------")

#-----------------------------------------------------------------------------------------------------------------------

# Display topper based on total marks
topper = max(totals, key=totals.get)
print("Topper Based on Total Marks:")
print(topper, ":", totals[topper])
print("--------------------------------------------------------------------------------------------------------------------")

#-----------------------------------------------------------------------------------------------------------------------------

# Display subject-wise highest marks
subjects = ["Math", "Science", "English"]

print("Subject-wise Highest Marks:")
for subject in subjects:
    highest_student = ""
    highest_marks = 0

    for student in students:
        if students[student][subject] > highest_marks:
            highest_marks = students[student][subject]
            highest_student = student

    print(subject, ":", highest_student, "-", highest_marks)
print("-----------------------------------------------------------------------------------------------------------------------------")

#-----------------------------------------------------------------------------------------------------------------------------------


# Display students whose average is >= 85
print("Students with Average Marks >= 85:")

for student, marks in students.items():
    average = sum(marks.values()) / len(marks)
    if average >= 85:
        print(student, ":", average)

print("--------------------------------------------------------------------------------------------------------------------------")
#---------------------------------------------------------------------------------------------------------------------------------

'''Output:
Aman
Total Marks = 257
Average Marks = 85.66666666666667
Jake
Total Marks = 254
Average Marks = 84.66666666666667
Ankit
Total Marks = 261
Average Marks = 87.0
---------------------------------------------------------------------------------------------------------
Topper Based on Total Marks:
Ankit : 261
---------------------------------------------------------------------------------------------------------
Subject-wise Highest Marks:
Math : Aman - 87
Science : Ankit - 83
English : Ankit - 93
---------------------------------------------------------------------------------------------------------
Students with Average Marks >= 85:
Aman : 85.66666666666667
Ankit : 87.0
---------------------------------------------------------------------------------------------------------
'''

    