'''------------------------------------------------- Hospital Emergency Triage System ----------------------------------------------------

A hospital prioritizes patients based on: 
• Critical Condition  
• Age  
• Oxygen Level  
Rules: 
• Critical condition → Immediate Treatment  
• Oxygen below 90 → High Priority  
• Age above 65 → Medium Priority  
• Others → Normal Priority  
-------------------------------------------------------------------------------------------------------------------------------------------
Sample Input 
Critical Condition (Y/N): N 
Age: 70 
Oxygen Level: 94 
-------------------------------------------------------------------------------------------------------------------------------------------
Sample Output 
Patient Priority: Medium Priority 
Reason: Senior Citizen 
-------------------------------------------------------------------------------------------------------------------------------------------
'''

#------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------Coding------------------------------------------------------------------

# taking critical condition input from the user
critical_condition = input("Enter Critical Condition (Y/N) : ")

# taking age input from the user
age = int(input("Enter Age : "))

# taking oxygen level input from the user
oxygen_level = int(input("Enter oxygen level : "))

print("------------------------------------------------------------------------------------------------------------------------------------")

#------------------------------------------------------------------------------------------------------------------------------------------

# validating age input

if (age <= 0):
    exit("Invalid input ! Age must be positive")

# validating oxygen level input 

if (oxygen_level <= 0):
    exit("Invalid input ! oxygen level must be positive")

#-------------------------------------------------------------------------------------------------------------------------------------------
 
# displaying patient priority based on condition on input

if (critical_condition == 'Y'):
    print("Immediate Treatment")
    print("Reason : Critical Condition") 
elif (oxygen_level < 90):
    print("High Priority") 
    print("Reason : Oxygen level below 90")
elif (age  > 65):
    print("Medium Priority")
    print("Senior Citizen")
else:
    print("Normal Priority")

#-----------------------------------------------------------------------------------------------------------------------------------------

'''Output:
Enter Critical Condition (Y/N) : Y
Enter Age : 44
Enter oxygen level : 98
------------------------------------------------------------------------------------------------------------------------------------
Immediate Treatment
Reason : Critical Condition
'''

