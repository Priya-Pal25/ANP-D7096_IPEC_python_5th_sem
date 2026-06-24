"""Write a Python program to calculate the remaining balance after withdrawal."""

Current_Balance = float(input("Enter the Current Balance (in Rs):" ))
Withdrawal_Amount = float(input("Enter the Withdrawal Amount (in Rs) : " ))

print("Remaining Balance : " , (Current_Balance - Withdrawal_Amount))