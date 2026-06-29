'''--------------------------------------------Login System with Maximum Attempts---------------------------------------------------- 

A system allows only three login attempts. 
The correct username is admin and the password is python123. 
If the credentials are correct, display "Login Successful". 
Otherwise, after three unsuccessful attempts, display "Account Locked". 
---------------------------------------------------------------------------------------------------------------------------------------
Sample Output 
Attempt 1 
Username: admin 
Password: abc 
-----------------------------------------------------------------------------------------------------------------------------------
 
Invalid Credentials 
-----------------------------------------------------------------------------------------------------------------------------------------
 
Attempt 2 
Username: admin 
Password: python123 
-----------------------------------------------------------------------------------------------------------------------------------------
 
Login Successful
--------------------------------------------------------------------------------------------------------------------------------------------
'''

#----------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------Coding----------------------------------------------------------------------

correct_username = 'admin' 
correct_Password = 'python123'

#-------------------------------------------------------------------------------------------------------------

# checking if the user has enter correct credential or not

for x in range(1,4):
    user_name = input("Enter username: ")
    password = input("Enter Password : ")
    print("Attempt " , x)

    if (user_name == correct_username and password == correct_Password):
        print("login successful")
        break


    else:
        print("Invalid Credential")
    if (x >= 3):    
        print("Account locked")

#-----------------------------------------------------------------------------------------------------------------------------------

'''Output:
Enter username: admin
Enter Password : gfe
Attempt  1
Invalid Credential
Enter username: hi
Enter Password : 123
Attempt  2
Invalid Credential
Enter username: admin
Enter Password : python123
Attempt  3
login successful
'''