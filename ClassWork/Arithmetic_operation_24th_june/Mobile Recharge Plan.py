'''Write a Python program to calculate the total recharge amount based on the data pack selected.'''

cost = float(input("Enter the Cost per GB : "))
number_of_gbs =  int(input ("Enter number of GBs : "))

print("Total Recharge Cost : ",(cost * number_of_gbs))