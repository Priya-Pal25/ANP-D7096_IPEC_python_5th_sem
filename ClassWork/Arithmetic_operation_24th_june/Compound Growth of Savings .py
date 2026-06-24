'''Write a Python program to calculate the value of money after a certain number of years assuming it 
doubles every year.'''

Initial_Amount = float(input("Enter Initial Amount : "))
Number_of_years = int(input("Enter the Number of years : "))

print("Final Amount : " , (Initial_Amount * Number_of_years * 2))