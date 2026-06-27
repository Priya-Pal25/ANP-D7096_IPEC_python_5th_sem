'''Write a Python program to calculate the total recharge amount based on the data pack selected.'''

# Taking input from the user

cost = float(input("Enter the Cost per GB : "))
number_of_gbs =  float(input ("Enter number of GBs : "))
#---------------------------------------------------------------------------------------------------------

# Displaying the input to the user

print("Cost per GB : " ,cost)
print("Number of Gbs : ",number_of_gbs)
#---------------------------------------------------------------------------------------------------------

# Displaying the Total Recharge Cost

print("Total Recharge Cost : ",(cost * number_of_gbs))
#----------------------------------------------------------------------------------------------------------

'''Output:
Enter the Cost per GB : 85.0
Enter number of GBs : 1.5 
Cost per GB :  85.0
Number of Gbs :  1.5
'''