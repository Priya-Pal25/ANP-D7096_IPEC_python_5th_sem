'''-------------------------------------------Bank Transaction Summary------------------------------------------------------------- 
 
A customer keeps entering transaction amounts. 
Positive numbers indicate deposits, while negative numbers indicate withdrawals. 
The customer enters 0 to finish. 
-------------------------------------------------------------------------------------------------------------------------------
Display: 
• Total Deposit  
• Total Withdrawal  
• Final Balance
--------------------------------------------------------------------------------------------------------------------------------
'''

#------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------Coding--------------------------------------------------------------------



total_deposit = 0
total_Withdraw = 0
final_balance = 0

while(True):
    # taking input from user
    amount = float(input("Enter the Transaction amount (0 to stop) : "))

    
    if amount == 0:
        break
    elif amount > 0:
        total_deposit = total_deposit + amount

    else:
        total_Withdraw = total_Withdraw + amount

    final_balance = final_balance + amount

# Displaying total deposit
print("Total Deposit :", total_deposit)

# Displaying total withdrawal
print("Total Withdrawal :", total_Withdraw)

# Displaying final balance
print("Final Balance :", final_balance)

#---------------------------------------------------------

'''Output:
Enter the Transaction amount (0 to stop) : 54000
Enter the Transaction amount (0 to stop) : -5000
Enter the Transaction amount (0 to stop) : 0
Total Deposit : 54000.0
Total Withdrawal : -5000.0
Final Balance : 49000.0
'''

