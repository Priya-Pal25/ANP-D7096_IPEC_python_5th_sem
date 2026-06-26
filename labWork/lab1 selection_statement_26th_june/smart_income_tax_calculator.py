''''----------------------------Smart Income Tax Calculator -------------------------------------

A government tax portal calculates tax based on the following conditions: 
• Income up to ₹5,00,000 → No tax  
• ₹5,00,001 to ₹10,00,000 → 10%  
• ₹10,00,001 to ₹20,00,000 → 20%  
• Above ₹20,00,000 → 30%  
Additional Benefits: 
• Senior citizens (Age ≥ 60) receive a 5% rebate on tax.  
• Women taxpayers receive an additional 2% rebate on tax.  
Write a Python program to calculate the final tax amount payable. 
------------------------------------------------------------------------------------------------
Sample Input 
Enter Annual Income: 1200000 
Enter Age: 65 
Enter Gender (M/F): F 
---------------------------------------------------------------------------------------------------
Sample Output 
Tax before rebate: ₹240000.0 
Senior Citizen Rebate: ₹12000.0 
Women Rebate: ₹4800.0 
Final Tax Payable: ₹223200.0
--------------------------------------------------------------------------------------------------
'''
#------------------------------------------------------------------------------------------------
#----------------------------------------------Coding--------------------------------------------

# Taking income input from the user
income = float(input("Enter Annual Income: "))

# Taking age input from the user
age = int(input("Enter Age: "))

# Taking gender input from the user
gender = input("Enter Gender (M/F): ")

print("--------------------------------------------------------------------------------------")
#-------------------------------------------------------------------------------------------------

# Validating annual income
if (income <= 0):
    exit("Annual Income must be positive")

# validating age
if(age <= 0):
    exit("Age must be positive")

#-------------------------------------------------------------------------------------------------------


# Calculating tax
if (income <= 500000):
    tax = 0
elif (income <= 1000000):
    tax = income * 0.10
elif (income <= 2000000):
    tax = income * 0.20
else:
    tax = income * 0.30

print("Tax before rebate: ", tax)

#---------------------------------------------------------------------------------------------------------

# Senior citizen rebate
senior_rebate = 0
if (age >= 60):
    senior_rebate = tax * 0.05
print("Senior Citizen Rebate: ", senior_rebate)

#----------------------------------------------------------------------------------------------------------

# Women rebate
women_rebate = 0
if (gender == "F"):
    women_rebate = tax * 0.02
    print("Women Rebate: ", women_rebate)

#-------------------------------------------------------------------------------------------------------


print("Final Tax Payable: ", tax - senior_rebate - women_rebate)

#--------------------------------------------------------------------------------------------------------

'''Output:
Tax before rebate:  300000.0
Senior Citizen Rebate:  15000.0
Final Tax Payable:  285000.0
'''