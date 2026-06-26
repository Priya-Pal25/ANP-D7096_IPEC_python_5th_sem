''' ------------------------------------- University Scholarship System -----------------------------------------

Scholarship is awarded based on percentage: 
Percentage Scholarship 
95+ -> 100% 
90-94 -> 75% 
85-89 -> 50% 
80-84 -> 25% 
Below 80 -> No Scholarship 
----------------------------------------------------------------------------------------------------------------
Conditions: 
• Family income must be below ₹8,00,000.  
• Students with disciplinary actions receive no scholarship.  
-------------------------------------------------------------------------------------------------------------
Sample Input 
Percentage: 92 
Family Income: 500000 
Disciplinary Action (Y/N): N 
------------------------------------------------------------------------------------------------------------
Sample Output 
Scholarship Awarded: 75%
-------------------------------------------------------------------------------------------------------------
'''

#------------------------------------------------------------------------------------------------------------
#-----------------------------------------Coding-------------------------------------------------------------

# Taking percentage input from the user
percentage = float(input("Enter Percentage (in %): "))

# Taking family income input from the user
income= float(input("Enter Income (in Rs): "))

## Taking disciplinary action input from the user
action= input("Enter Disciplinary action (Y/N): ")

print("--------------------------------------------------------------------------------------")
#-------------------------------------------------------------------------------------------------

# Validating percentage
if (percentage <= 0):
    exit("Percentage must be positive")

# validating income
if(income <= 0):
    exit("Income must be positive")

#-------------------------------------------------------------------------------------------------------

# Students with disciplinary actions receive no scholarship
if (action == 'Y'):
    exit("Students with disciplinary actions receive no scholarship")

# Calculating scholarship
if (income < 800000):
    if (percentage >= 95):
        print("Scholarship Awarded: 100%")
    elif (percentage >= 90 and percentage <= 94 ):
        print("Scholarship Awarded: 75%")
    elif (percentage >= 85 and percentage <= 89):
        print("Scholarship Awarded: 50%")
    elif (percentage >= 80 and percentage <= 84):
        print("Scholarship Awarded: 25%")
    else:
        print("No Scholarship ")
else:
    print("Income is greater then 800000")  
    print("No Scholarship")      


#---------------------------------------------------------------------------------------------------------

'''Output:
Enter Percentage (in %): 95
Enter Income (in Rs): 175000
Enter Disciplinary action (Y/N): N
--------------------------------------------------------------------------------------
Scholarship Awarded: 100%
'''
