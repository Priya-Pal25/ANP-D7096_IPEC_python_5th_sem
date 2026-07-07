'''--------------------------------------------- Password Strength Checker------------------------------------------------ 
Write a function check_password(password) that checks whether a password is strong. 
A password is considered Strong if: 
• It contains at least 8 characters.  
• It contains at least one uppercase letter.  
• It contains at least one lowercase letter.  
• It contains at least one digit.  
The function should return: 
• "Strong Password" or  
• "Weak Password"  
The main program should accept a password from the user and display the result.
'''

#-----------------------------------------------------------------------------------------------------------------------
#-------------------------------------------- Coding ------------------------------------------------------------------

# function to check password

def check_password(password):
    if len(password) >= 8:
        for x in password:
            if (x.isupper()):
                upper = True
            if (x.islower()):
                lower = True
            if (x.isdigit()):
                digit = True
        if (upper and lower and digit):
            return 'Strong Password'
    else:
        return 'Weak Password'
    
#-----------------------------------------------------------------------------------------------------------------------------

# main program

# taking user input
password= input("Enter the password : ")
print("--------------------------------------------------------------------------------------------------------")

#--------------------------------------------------------------------------------------------------------------

# displaying the result
print("The Password enter by the user is ", check_password(password))

#----------------------------------------------------------------------------------------------------------------

'''Output:
Enter the password : Admin78989
--------------------------------------------------------------------------------------------------------
The Password enter by the user is  Strong Password
'''