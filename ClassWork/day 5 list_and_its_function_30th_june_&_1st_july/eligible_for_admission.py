'''Write a program to create a list of marks of 15 students alomg with their name.
display the name of students who are eligibile for admission
a student will be eligible if the marks will greater than 70'''

# creating list
name = []
marks = []

print("Enter details of 10 students")

# taking input from user 

for i in range(10):
    n = input("Enter student name: ")
    m = int(input("Enter marks: "))
    name.append(n)
    marks.append(m)
print("------------------------------------------------------")
#--------------------------------------------------------------
print("Students eligible for admission:")

# checking the eligibility
for i in range(10):
    if marks[i] > 70:
        print(name[i])

#--------------------------------------------------------------

'''Output:
Enter details of 10 students
Enter student name: riya
Enter marks: 56
Enter student name: rohit
Enter marks: 57
Enter student name: anmol
Enter marks: 85
Enter student name: renuka
Enter marks: 85
Enter student name: aarushi 
Enter marks: 86
Enter student name: shreya
Enter marks: 86
Enter student name: yogesh
Enter marks: 75
Enter student name: akansha
Enter marks: 81
Enter student name: garv
Enter marks: 78
Enter student name: priya
Enter marks: 88
---------------------------------------------------
Students eligible for admission:
anmol
renuka
aarushi 
shreya
yogesh
akansha
garv
priya
'''