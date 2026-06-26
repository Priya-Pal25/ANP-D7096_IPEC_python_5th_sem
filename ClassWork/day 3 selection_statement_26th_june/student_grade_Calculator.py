''' ---------------------------Student Grade Calculator------------------------------------ 
A school assigns grades based on the marks obtained by students according to the following criteria: 
• Marks 90 and above → Grade A  
• Marks 75 to 89 → Grade B  
• Marks 50 to 74 → Grade C  
• Below 50 → Grade F  
Write a Python program to accept marks from the user and display the corresponding grade. 
----------------------------------------------------------------------------------------------------
Sample Input 
Enter Marks: 92 
----------------------------------------------------------------------------------------------------
Sample Output 
Grade A 
-----------------------------------------------------------------------------------------------------
Sample Input 
Enter Marks: 80 
-----------------------------------------------------------------------------------------------------
Sample Output 
Grade B 
-----------------------------------------------------------------------------------------------------
Sample Input 
Enter Marks: 65 
------------------------------------------------------------------------------------------------------
Sample Output 
Grade C 
----------------------------------------------------------------------------------------------------
Sample Input 
Enter Marks: 35 
-----------------------------------------------------------------------------------------------------
Sample Output 
Grade F
----------------------------------------------------------------------------------------------------
'''
#-------------------------------------------------------------------------------------------------
#---------------------------------Coding----------------------------------------------------------

# Taking marks input from the user

marks = float(input("Enter the Marks(out of 100): "))

# validating marks
if (marks <=0):
    exit(" Invalid Marks")

# Calculating grade
if (marks >= 90):
    print("Grade A")
elif(marks >= 75 and marks <=89):
    print("Grade B")
elif(marks >= 50 and marks <= 74):
    print("Grade C")
else:
    print("Grade F")    

#-------------------------------------------------------------------------------
'''Output:
Enter the Marks(out of 100): 95
Grade A
'''