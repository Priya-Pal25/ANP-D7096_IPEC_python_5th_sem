'''Student Result Analyzer 

A teacher wants to analyze the marks of N students. 
Accept the marks of each student (out of 100). 
Finally display: 
• Highest Marks  
• Lowest Marks  
• Average Marks  
• Number of students who passed (Marks ≥ 40)  
• Number of students who scored distinction (Marks ≥ 75)  
'''

#-----------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------Coding-------------------------------------------------------------------------

# Taking input from the user
student = int (input("Enter the no of student : "))


#---------------------------------------------------------------------------------------------------------------

# Validating student

if (student <= 0):
    exit("Number of student must be positive")

#-------------------------------------------------------------------------------------------------------------------

total_marks = 0
count_pass = 0
count_dist = 0

# Accepting the marks of each student
for x in range(1,student+1):
    marks = float(input("Enter the marks(out of 100): "))

    # validating marks

    if (marks <= 0):
        exit("Student marks must be positive")

    #-------------------------------------------------------------------------------------------------------------------

    # Calulating total marks
    total_marks = total_marks +marks

    #------------------------------------------------------------------------------------------------------------------
    #  analyzing marks of N student

    if x == 1:
        highest = marks
        lowest= marks

    
    else:
        if (marks > highest):
            highest = marks
        if (marks < lowest):
            lowest = marks
        
    if (marks >= 40):
        count_pass = count_pass +1

    if (marks >= 75):
        count_dist = count_dist + 1


#-------------------------------------------------------------------------------------------------------------------

# Calculate and display highest marks
print("Highest marks : ",highest)

# Calculate and display lowest marks 
print("Highest marks:",lowest)

# Calculate and display average marks
print("Average marks: ",(total_marks/student))

# Calculate and display the no of who passed (Marks ≥ 40) 
print("Number of student who passed : ",count_pass)

# Calculate and display the Number of students who scored distinction (Marks ≥ 75) 
print("Number of student who scored distinction : ",count_dist)
#-------------------------------------------------------------------------------------------------------------------------

'''output:
Enter the no of student : 5
Enter the marks(out of 100): 455
Enter the marks(out of 100): 87
Enter the marks(out of 100): 996
Enter the marks(out of 100): 85
Enter the marks(out of 100): 84
Highest marks :  996.0
Highest marks: 84.0
Average marks:  341.4
Number of student who passed :  5
Number of student who scored distinction :  5
'''