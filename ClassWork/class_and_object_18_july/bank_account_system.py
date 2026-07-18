'''-----------------------------------Problem 2: Bank Account System-------------------------------------- 
Problem Statement 
Create a simple Bank Account class that allows users to deposit and withdraw money. 
Requirements 
1. Create a class BankAccount.  
2. Define the following instance variables:  
o account_number  
o customer_name  
o balance  
3. Create the following methods:  
o accept_details() - Accept account details from the user.  
o deposit(amount) - Add the amount to the balance.  
o withdraw(amount) - Deduct the amount if sufficient balance is available; otherwise 
display "Insufficient Balance".  
o display_balance() - Display account details and current balance.  
4. Create an object of the class.  
5. Accept a deposit amount and a withdrawal amount from the user and perform both operations.  
Sample Input 
Enter Account Number : 1001 
Enter Customer Name : Anjali 
Enter Initial Balance : 5000 
 
Enter Deposit Amount : 2000 
Enter Withdrawal Amount : 4500 
Expected Output 
Deposit Successful. 
 
Withdrawal Successful. 
 ------ Account Details ------ 
Account Number : 1001 
Customer Name  : Anjali 
Current Balance: 2500 
Sample Output (Insufficient Balance) 
Enter Withdrawal Amount : 9000 
 
Insufficient Balance. 
 ------ Account Details ------ 
Account Number : 1001 
Customer Name  : Anjali 
Current Balance: 7000 
'''

#------------------------------------------------------------------------------------------------------------
#---------------------------------------------Coding---------------------------------------------------------

class BankAccount:
    def __init__(self):
        self.account_number = 0
        self.customer_name = ""
        self.balance = 0

    def accept_deatils(self):
        self.account_number = int(input("Enter the account number : "))
        self.customer_name = input("Enter customer name : ")
        self.balance = float(input("Enter the Initial balance : "))

    def deposit(self ,deposit_amount):
        self.balance = self.balance + deposit_amount
        print("Deposite successful")

    def withdraw(self,amount):
        
        if (amount < self.balance):
            print("Withdrawal successful")
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("Account Number : ",self.account_number)
        print("Customer name : " ,self.customer_name)
        print("Initial Balance : ",self.balance)

#-----------------------------------------------------------------------------------------------
#--------------------------------------main program---------------------------------------------

e1 = BankAccount()
e1.accept_deatils()
deposit_amount = float(input("Enter the deposit amount : "))
e1.deposit(deposit_amount)
withdraw_amount = float(input("Enter the withdrawal amount : "))
e1.withdraw(withdraw_amount)
e1.display_balance()

#------------------------------------------------------------------------------------------------

'''Output :
Enter the account number : 101
Enter customer name : hina
Enter the Initial balance : 5000
Enter the deposit amount : 2500
Deposite successful
Enter the withdrawal amount : 2500
Withdrawal successful
Account Number :  101
Customer name :  hina
Initial Balance :  7500.0
'''

#---------------------------------------------------------------------------------------------


