''' -------------------------------Online Examination Result Analyzer ----------------------------------

A student appears in 5 subjects. 
Rules: 
• Minimum 40 marks in every subject to pass.  
• Distinction → Average ≥ 75  
• First Division→ Average ≥ 60  
• Second Division → Average ≥ 50  
• Pass  → Average ≥ 40  
• Fail if any subject score < 40 
------------------------------------------------------------------------------------------------------
Sample Input 
Hindi : 85 
English : 78 
Mathematics : 82 
Science : 75 
Computer : 90 
-------------------------------------------------------------------------------------------------------
Sample Output 
Average Marks: 82.0 
Result: PASS 
Classification: Distinction 
-------------------------------------------------------------------------------------------------------
'''

#--------------------------------------------------------------------------------------------------------
#----------------------------------------------Coding----------------------------------------------------

# Taking hindi marks from the user
hindi = float(input("Enter Hindi marks (out of 100) : "))

# Taking english marks from the user
english = float(input("Enter English marks (out of 100) : "))

# Taking maths marks from the user
maths = float(input("Enter Mathematics marks (out of 100) : "))

# Taking science marks from the user
science = float(input("Enter Science marks (out of 100) : "))

# Taking computer marks from the user
computer = float(input("Enter Computer marks (out of 100) : "))


print("-------------------------------------------------------------------------------------------------")

#-----------------------------------------------------------------------------------------------------------

# validating hindi marks
if (hindi <= 0):
    exit("Hindi marks must be positive")

# validating english marks
if (english <= 0):
    exit("English marks must be positive")

# validating maths marks
if (maths <= 0):
    exit("Mathematics marks must be positive")

# validating science marks
if (science <= 0):
    exit("Science marks must be positive")

# validating computer marks
if (computer <= 0):
    exit("Computer marks must be positive")
#------------------------------------------------------------------------------------------------------------------------------

# calculating average

avg = (hindi + english + maths + science + computer)/5
print("Average marks: " ,avg)

#--------------------------------------------------------------------------------------------------------------------------------

# calculating result

if (hindi >= 40 and english >= 40 and maths >= 40 and science >= 40 and computer >= 40):
    
      
    if (avg >= 75):
        print("Result : PASS")
        print("Classification : DISTINCTION")
    elif (avg >= 60 ):
        print("Result : PASS")
        print("Classification : FIRST DIVISION")
    elif (avg >= 50):
        print("Result : PASS")
        print("Classification : SECOND DIVISION")
    elif (avg >= 40):
        print("Result : PASS")
        print("classification : PASS")
    else:
        print("Result : FAIL")

else:
    print("Result : FAIL")

#-------------------------------------------------------------------------------------------------------------------------------


'''Output:
Enter Hindi marks (out of 100) : 89
Enter English marks (out of 100) : 90
Enter Mathematics marks (out of 100) : 91
Enter Science marks (out of 100) : 92
Enter Computer marks (out of 100) : 93
-------------------------------------------------------------------------------------------------
Average marks:  91.0
Result : PASS
Classification : DISTINCTION

'''
