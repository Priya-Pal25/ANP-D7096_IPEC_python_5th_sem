'''---------------------------------------- Restaurant Bill Discount---------------------------------------- 

A restaurant offers discounts based on the total bill amount. 
• Bill below ₹1000 → No Discount  
• ₹1000 - ₹2999 → 10% Discount  
• ₹3000 or more → 20% Discount  
Write a Python program to determine the applicable discount. 
------------------------------------------------------------------------------------------------------------
Sample Input 
3200 
-----------------------------------------------------------------------------------------------------------
Sample Output 
20% Discount Applied
-----------------------------------------------------------------------------------------------------------
'''

#----------------------------------------------------------------------------------------------------------
#----------------------------------------Coding------------------------------------------------------------

# Taking total bill amount input from the user

total_bill_amount = float(input("Enter total bill amount: " ))

print("-----------------------------------------------------------------------------------------------------")

#------------------------------------------------------------------------------------------------------------

# Validating bill amount

if (total_bill_amount <= 0):
    exit("Invalid Input")

#---------------------------------------------------------------------------------------------------------------

# Determining and display the applicable discount

if (total_bill_amount < 1000):
    
    print("No Discount")

elif (total_bill_amount >= 1000 and total_bill_amount <= 2999):
    discount = total_bill_amount * 0.10
    print("10% Discount Applied")

else:
    discount = total_bill_amount * 0.20
    print("20% Discount Applied")

final = total_bill_amount - discount
print("Final bill amount : ",final)

#------------------------------------------------------------------------------------------------------------------

'''Output:
Enter total bill amount: 3200
-----------------------------------------------------------------------------------------------------
20% Discount Applied
Final bill amount :  2560.0
'''
