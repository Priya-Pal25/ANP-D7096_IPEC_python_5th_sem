'''-----------------------------Multi-Level Access Control System------------------------------------------------------------------- 

Assign access levels based on: 
Roles: 
• Admin  
• Manager  
• Employee  
• Guest  
-------------------------------------------------------------------------------------------------------------------------------------
Conditions: 
• Admin + Security Clearance ≥ 5 → Full Access  
• Manager + Experience > 5 Years → Department Access  
• Employee + Experience > 2 Years → Limited Access  
• Guest → Read-Only Access  
• Inactive Account → No Access  
-------------------------------------------------------------------------------------------------------------------------------------
Sample Input 
Role: Admin 
Security Clearance: 6 
Account Status: Active 
--------------------------------------------------------------------------------------------------------------------------------------
Sample Output 
Access Level: FULL ACCESS
--------------------------------------------------------------------------------------------------------------------------------------
'''

#--------------------------------------------------------------------------------------------------------
#----------------------------------------------Coding----------------------------------------------------

# Taking role input from the user
role = input("Enter Role ( Admin/ Manager/ Employee/ Guest) : ")


# Taking Account status input from the user
status = input("Enter Account Status (Active / Inactive) : ")

print("-------------------------------------------------------------------------------------------------")

#-----------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------------------------------------------------

# Displaying Access to tthe user based on the condition and role


if (status == 'Active'):
    if (role == 'Admin'):
        security = int(input("Enter Security Clearance : "))
        if (security >= 5):
         print("Access Level : FULL ACCESS")



    elif ( role == 'Manager' ):
        experience = int(input("Enter Experience (in years) : "))
        if (experience > 5):
            print("Access Level : DEPARTMENT ACCESS")

    elif (role == 'Employee' ):
        experience = int(input("Enter Experience (in years) : "))
        if (experience > 2):
            print("Limited Access")
    
    else:
        print("Read - Only Access")

else:
    print("Inactive Account ! No Access")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Output:
Enter Role ( Admin/ Manager/ Employee/ Guest) : Admin
Enter Account Status (Active / Inactive) : Active
-------------------------------------------------------------------------------------------------
Enter Security Clearance : 7
Access Level : FULL ACCESS
'''