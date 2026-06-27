'''Write a Python program to calculate the remaining balance after withdrawal.'''

#taking input from the user

Current_Balance = float(input("Enter the Current Balance (in Rs):" ))
Withdrawal_Amount = float(input("Enter the Withdrawal Amount (in Rs) : " ))
#------------------------------------------------------------------------------------------------

#displaying the input to the user
print("Current Balance(in Rs): " ,Current_Balance)
print("Withdrawal Amount (in Rs): " ,Withdrawal_Amount)
#------------------------------------------------------------------------------------------------

#displaying the remaining balance to the user

print("Remaining Balance : " , (Current_Balance - Withdrawal_Amount))

#-------------------------------------------------------------------------------------------------
'''Output:
Enter the Current Balance (in Rs):5000.0
Enter the Withdrawal Amount (in Rs) : 2500.0
Current Balance(in Rs):  5000.0
Withdrawal Amount (in Rs):  2500.0
Remaining Balance :  2500.0
'''