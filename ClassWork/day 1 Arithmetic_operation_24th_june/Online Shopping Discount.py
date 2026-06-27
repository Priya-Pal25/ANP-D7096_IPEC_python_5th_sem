'''Write a Python program to calculate the final payable amount after applying the discount. '''

# Taking input from the user

product_price = float(input("Enter the Price of the Product : "))
Discount_Amount = float(input("Enter the Discount Amount : "))
#------------------------------------------------------------------------------------------------

# Displaying the input to the user

print("Price of the Product: " ,product_price)
print("Discount Amount: " ,Discount_Amount)
#-------------------------------------------------------------------------------------------------

# Displaying the Final Price to the user
 
print("Final Price : " ,(product_price - Discount_Amount) ) 
#--------------------------------------------------------------------------------------------------

'''Output:
Enter the Price of the Product : 500.0
Enter the Discount Amount : 100.0
Price of the Product:  500.0
Discount Amount:  100.0
Final Price :  400.0
'''