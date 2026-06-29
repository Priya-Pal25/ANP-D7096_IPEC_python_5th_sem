'''---------------------------------Cybersecurity Login Validation ---------------------------------------
 
A login system validates: 
• Username  
• Password  
• OTP  
---------------------------------------------------------------------------------------------------------
Conditions: 
• All correct → Login Successful  
• Incorrect OTP → Re-enter OTP  
• Incorrect Password after 3 attempts → Account Locked  
• Incorrect Username → User Not Found  
------------------------------------------------------------------------------------------------------------
Sample Input 
Username: admin 
Password: admin123 
OTP: 4567 
--------------------------------------------------------------------------------------------------------------
Sample Output 
Login Successful 
Welcome Admin
----------------------------------------------------------------------------------------------------------
'''

#------------------------------------------------------------------------------------------------------------
#-----------------------------------------Coding-------------------------------------------------------------

# correct credential
correct_username = "admin"
correct_password = "admin123"
correct_otp = 4567

# Taking input from the user
username = input("Enter Username : ")
password= input("Enter Password : ")
otp= int(input("Enter four digit OTP : "))

print("--------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------

# Validating otp
if (otp <= 0):
    exit("OTP must be positive")

#----------------------------------------------------------------------------------------------------------

if (username == correct_username and password == correct_password and otp == correct_otp):
    print("Login Successful")
elif (otp != correct_otp):
    print("Re-Enter otp")
elif (username != correct_username):
    print("User Not Found")

   
else:
    for x in range(1,4):
        password = input("Enter Password: ")

        
        if password == correct_password:
            break 

        if x == 3:
            print("Account Locked")
            break

        
        print("Incorrect Password. Try Again.")

#-------------------------------------------------------------------------------------------------------------------------

'''Output:
Enter Username : admin
Enter Password : admin123
Enter four digit OTP : 4567
--------------------------------------------------------------------------------------
Login Successful
'''

    
