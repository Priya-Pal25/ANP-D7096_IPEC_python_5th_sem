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

while (num != secret_num):
    if (num < secret_num):
        print("Number is too low")
        num = int(input("Enter number: "))
    else:
        print("Number is too high")
        num = int(input("Enter number: "))
print("The number is correct")

#-----------------------------------------------------------------------------------------------------------------

'''Output:
Enter number: 45
----------------------------------------------------------------------------------------------------
Number is too high
Enter number: 25
Number is too low
Enter number: 37
The number is correct
'''