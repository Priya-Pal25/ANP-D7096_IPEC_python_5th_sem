'''--------------------------Secure Vault Access------------------------------------------------------- 

A digital vault can only be opened if the user enters the correct security code. 
Write a Python program that accepts the entered security code. If the entered code is 7890, display: 
"Access Granted to the Vault." 
Otherwise, do nothing. 
--------------------------------------------------------------------------------------------------------
Sample Input 
7890 
--------------------------------------------------------------------------------------------------------
Sample Output 
Access Granted to the Vault.
--------------------------------------------------------------------------------------------------------
'''

#------------------------------------------------------------------------------------------------------
#--------------------------------------------Coding---------------------------------------------------

# Taking security code input from the user

security_code = int(input("Enter the Security Code: " ))

print("-------------------------------------------------------------")

#-------------------------------------------------------------------------------------------------------

# validating security code

if(security_code <= 0):
    exit("Security Code must be positive")

#--------------------------------------------------------------------------------------------------------

# Checking whether the access should be given or not

if (security_code == 7890):
    print("Access Granted to the Vault.")


#---------------------------------------------------------------------------------------------------------

'''Output:
Enter the Security Code: 7890
-------------------------------------------------------------
Access Granted to the Vault.
'''

