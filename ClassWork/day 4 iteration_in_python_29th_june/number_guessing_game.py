'''---------------------------------Number Guessing Game-------------------------------------- 

A secret number is 37. 
Keep asking the user to guess the number until the correct number is entered. 
Display whether the entered number is too high, too low, or correct.
----------------------------------------------------------------------------------------------- 
'''

#---------------------------------------------------------------------------------------------

# Taking input from the user

num = int(input("Enter number: "))

print("----------------------------------------------------------------------------------------------------")

#---------------------------------------------------------------------------------------------------------------

secret_num = 37

while (secret_num != 37):
    if (secret_num < 37):
        print("Number is too low")
        num = int(input("Enter number: "))
    ele:
        print("Number is too high")
        num = int(input("Enter number: "))


    