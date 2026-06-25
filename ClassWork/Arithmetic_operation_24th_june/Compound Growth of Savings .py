'''Write a Python program to calculate the value of money after a certain number of years assuming it 
doubles every year.'''
# taking the input from the user

Initial_Amount = float(input("Enter Initial Amount : "))
Number_of_years = int(input("Enter the Number of years : "))
#-----------------------------------------------------------------------------------------

# displaying the input to the user
print("Initial Amount : " ,Initial_Amount)
print("Number of year : " ,Number_of_years)
#------------------------------------------------------------------------------------------

# displaying the final amount to the user

print("Final Amount : " , (Initial_Amount * Number_of_years * 2))
#--------------------------------------------------------------------------------------------

'''Output:
Enter Initial Amount : 50000.0
Enter the Number of years : 2
Initial Amount :  50000.0
Number of year :  2
Final Amount :  200000.0'''