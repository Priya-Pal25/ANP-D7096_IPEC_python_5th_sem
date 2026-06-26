'''-------------------------------------------E-Commerce Premium Membership Eligibility -------------------------
A customer becomes Premium Member if: 
• Total Purchases > ₹50,000  
• Orders Completed ≥ 20  
• Customer Rating ≥ 4.5  
------------------------------------------------------------------------------------------------------------------
Special Case: 
• Purchases above ₹1,00,000 automatically qualify.  
-----------------------------------------------------------------------------------------------------------------
Sample Input 
Total Purchases: 120000 
Orders Completed: 10 
Customer Rating: 4.0 
-----------------------------------------------------------------------------------------------------------------
Sample Output 
Premium Membership Status: Eligible 
Reason: Purchase amount exceeded ₹100000. 
-----------------------------------------------------------------------------------------------------------------
'''

#------------------------------------------------------------------------------------------------------
#----------------------------------------Coding--------------------------------------------------------

# Taking purchases input from the user
purchases = float(input("Enter Total purchases : "))

# Taking order completed input from the user
order = int(input("Enter Orders completed: "))

# Taking customer rating input from the user
rating = float(input("Enter customer rating: "))

print("---------------------------------------------------------------------------------------")

#-----------------------------------------------------------------------------------------------------

# validating purchaes
if(purchases <= 0):
    exit("Total purchases must be positive")

# validating order completed
if(order <= 0):
    exit("Order completed must be positive")

# validating customer rating
if(rating <= 0):
    exit("Customer rating must be positive")

#-------------------------------------------------------------------------------------------------------

# Purchases above ₹1,00,000 automatically qualify

if (purchases > 100000):
    print("Premium Membership Status: Eligible ")
    print("Reason: Purchase amount exceeded ₹100000")


elif (purchases > 50000 and order >= 20  and rating >= 4.5 ):
    print("Premium Membership Status: Eligible ")

else:
    print("Premium Membership Status: Not Eligible")

#-----------------------------------------------------------------------------------------------------------

'''Output:
Enter Total purchases : 85000
Enter Orders completed: 30
Enter customer rating: 5.0
---------------------------------------------------------------------------------------
Premium Membership Status: Eligible 
'''