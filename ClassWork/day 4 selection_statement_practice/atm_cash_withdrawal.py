'''. ATM Cash Withdrawal  

A customer can withdraw money only if the requested amount does not exceed the available balance. 
Accept the account balance and withdrawal amount. 
• If withdrawal amount is less than or equal to balance, display: 
Transaction Successful 
• Otherwise display: 
Insufficient Balance 
--------------------------------------------------------------------------------------------------------------
Sample Input 
5000 
4500 
--------------------------------------------------------------------------------------------------------------
Sample Output 
Transaction Successful
-------------------------------------------------------------------------------------------------------------
'''

#------------------------------------------------------------------------------------------------------------
#------------------------------------------Coding------------------------------------------------------------

available_amount = float(input("Enter the Available Balance : "))
withdrawal_amount = float(input("Enter the Wothdrawal Balance: "))

print("---------------------------------------------------------------------------------------------------")

#-----------------------------------------------------------------------------------------------------------

# validation of available amount 

if (available_amount <= 0):
    exit("Invalid Input! Available Balance must be positive")

# validation of withdrawal amount
if (withdrawal_amount <= 0):
    exit("Invalid Input! withdrawal Balance must be positive")

#----------------------------------------------------------------------------------------------------------------

# checking if the customer can withdraw money or not

if (withdrawal_amount <= available_amount):
    print("Transaction Successful")
    print("Current Balance : " , (available_amount - withdrawal_amount))

else:
    print("Insufficient Balance")

#-------------------------------------------------------------------------------------------------------------------

'''Output:
Enter the Available Balance : 5000
Enter the Wothdrawal Balance: 4500
---------------------------------------------------------------------------------------------------
Transaction Successful
Current Balance :  500.0
'''