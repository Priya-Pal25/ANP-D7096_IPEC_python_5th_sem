'''------------------------------------------Password Strength Checker---------------------------------- 

A website requires users to create a password having at least 8 characters. 
Keep asking the user to enter a password until the entered password satisfies the minimum length 
requirement. 
------------------------------------------------------------------------------------------------
Sample Output 
Enter Password: hello 
Password too short. 
---------------------------------------------------------------------------------------------------- 
Enter Password: python@123 
Password Accepted. 
------------------------------------------------------------------------------------------------------------'''

# Taking password input from the user

password =  input("Enter password : ")

#------------------------------------------------------------------------------------------------------------

minimum_length = 8
while(len(password) <= minimum_length):
    print("password too short")
    password =  input("Enter password : ")
print("Password Accepted")

#------------------------------------------------------------------------------------------------------------

'''Output:
Enter password : hello
password too short
Enter password : python@123
Password Accepted
'''