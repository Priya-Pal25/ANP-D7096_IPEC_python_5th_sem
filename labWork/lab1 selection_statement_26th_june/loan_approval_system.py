'''----------------------------------Loan Approval System ---------------------------------------

A bank evaluates loan applications using: 
• Credit Score ≥ 750  
• Annual Income ≥ ₹8,00,000  
• Existing Loan Amount ≤ ₹2,00,000  
Conditions: 
• All conditions satisfied → Approved  
• Only one condition fails → Manual Review  
• More than one condition fails → Rejected  
-------------------------------------------------------------------------------------------------
Sample Input 
Enter Credit Score: 780 
Enter Annual Income: 750000 
Enter Existing Loan Amount: 100000 
-------------------------------------------------------------------------------------------------
Sample Output 
Loan Status: Manual Review 
Reason: Income criteria not satisfied
-------------------------------------------------------------------------------------------------
'''

#------------------------------------------------------------------------------------------------
#-----------------------------------------Coding-------------------------------------------------

# Taking credit score input from the user 
credit_score = int(input("Enter Credit Score : "))

# Taking Annual income input from the user
income = float(input("Enter Annual Income: " ))

# Taking existing loan input from the user
existing_loan = float(input("Enter Existing Loan Amount : "))

#-------------------------------------------------------------------------------------------------
print("------------------------------------------------------------------------------------------------")

# validating Credit Score

if(credit_score <= 0):
    exit("Credit Score must be positive")

# validating Annual income

if(income <= 0):
    exit("Annual income must be positive")

# validating Existing loan
if(existing_loan <= 0):
    exit("Existing loam amount must be positive ")

#-------------------------------------------------------------------------------------------------
# verifying eligibility for loan


if (credit_score >= 750 and income >= 800000 and existing_loan <= 200000):
    print("Loan Status : Approved")
elif (credit_score >= 750 or income >= 800000 or existing_loan <= 200000 ):
    print("Loan Status : Manual Review")
    if (credit_score < 750):
        print("Reason : Credit criteria not satisfied")
    elif(income < 800000):
        print("Reason : Income criteria not satisfied")
    else:
        print("Reason : Existing loan criteria not satisfied")    

else:
    print("Loan Status : Rejected")

#----------------------------------------------------------------------------------------------------

'''Output:
Enter Credit Score : 800
Enter Annual Income: 1000000
Enter Existing Loan Amount : 100000
------------------------------------------------------------------------------------------------
Loan Status : Approved
'''



