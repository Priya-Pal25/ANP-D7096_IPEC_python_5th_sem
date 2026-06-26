''' --------------------------------------Employee Performance Evaluation ---------------------------

An employee is evaluated using: 
• Project Score  
• Attendance Percentage  
• Client Feedback Score  
Rules: 
• Excellent → All scores above 90  
• Good → Scores above 75  
• Average → Scores above 60  
• Poor → Otherwise  
-----------------------------------------------------------------------------------------------------
Additional Rule: 
• Attendance below 70% cannot receive more than Average rating.  
-----------------------------------------------------------------------------------------------------
Sample Input 
Project Score: 95 
Attendance: 65 
Client Feedback: 92 
------------------------------------------------------------------------------------------------------
Sample Output 
Performance Rating: Average 
Reason: Attendance below 70%
-------------------------------------------------------------------------------------------------------
'''

#------------------------------------------------------------------------------------------------------
#----------------------------------------Coding--------------------------------------------------------

# Taking project score input from the user
project_score = int(input("Enter Project Score (between 1 to 100) : "))

# Taking  Attendance percentage input from the user
attendance = float(input("Enter Attendance percentage (in %): "))

# Taking feedback score from the input user
feedback_score = int(input("Enter Client Feedback Score (between 1 to 100): "))

print("-----------------------------------------------------------------------------------------------")

#-----------------------------------------------------------------------------------------------------

# validating project score
if(project_score <= 0):
    exit("Project Score must be positive")

# validating attendance percentage
if(attendance <= 0):
    exit("Attendance percentage must be positive")

# validating client feedback score
if(feedback_score <= 0):
    exit("Client Feddback Score must be positive")

#-------------------------------------------------------------------------------------------------------

# Attendance below 70% cannot receive more than Average rating.

if (attendance < 70):
    print("Performance Rating : Average")
    print("Reason: Attendance below 70%")

#--------------------------------------------------------------------------------------------------------

# Evaluating the employee score

if (project_score > 90 and attendance > 90 and feedback_score > 90):
    print("Performance Rating : Excellent" )
elif (project_score > 75 and attendance > 75 and feedback_score > 75):
    print("Performance Rating : Good")
elif (project_score > 60 and attendance > 60 and feedback_score > 60):
    print("Performance Rating : Average")
else:
    print("Performance Rating : Poor")

#------------------------------------------------------------------------------------------------------

'''Output:
Enter Project Score (between 1 to 100) : 91
Enter Attendance percentage (in %): 97
Enter Client Feedback Score (between 1 to 100): 95
---------------------------------------------------------------------------------------------------------
Performance Rating : Excellent
'''