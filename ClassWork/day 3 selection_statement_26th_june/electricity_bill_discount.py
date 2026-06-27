'''------------------------------------------- Electricity Bill Discount ----------------------------- 
An electricity provider offers a 10% discount on the total bill amount if the customer's bill is ₹5,000 
or more. Otherwise, no discount is applied. 
Write a Python program to accept the total bill amount from the user and display the final amount to 
be paid. 

Sample Input 1 
Enter the electricity bill amount: 6200 
----------------------------------------------------
Sample Output 1 
Discount Applied! 
Final Bill Amount: ₹5580.0 
----------------------------------------------------
Sample Input 2 
Enter the electricity bill amount: 4200 
---------------------------------------------------
Sample Output 2 
No Discount Applied! 
Final Bill Amount: ₹4200
--------------------------------------------------'''

#------------------------------------------------------------------
#-------------------------Coding------------------------------------

# Taking electricity bill amount from the user
bill_amount = float(input("Enter the Electricity bill amount (in Rs): "))
# validating Electricity bill amount
if (bill_amount <= 0):
    exit("Electricity bill amount should be positive")
#----------------------------------------------------------------------
# Calculating bill_amount

if(bill_amount >= 5000):
    print("Discount Applied!")
    print("Final Bill Amount : " ,(bill_amount -(bill_amount * 0.10 )))

else:
    print("No Discount Applied")
    print("Final Bill Amount: " ,bill_amount ) 
#--------------------------------------------------------------------------

'''Output:
Enter the Electricity bill amount (in Rs): 9521
Discount Applied!
Final Bill Amount :  8568.9
'''

