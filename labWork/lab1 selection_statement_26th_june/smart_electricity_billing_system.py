'''-------------------------------Smart Electricity Billing System ---------------------------------------

Calculate electricity bill using: 
Units       Rate 
0-100      ₹5/unit 
101-300    ₹7/unit 
Above 300  ₹10/unit 
----------------------------------------------------------------------------------------------------------
Additional Rules: 
• Commercial consumers pay 20% extra.  
• Bills above ₹5000 attract 5% surcharge.  
• Senior citizens receive 10% discount.  
----------------------------------------------------------------------------------------------------------
Sample Input 
Units Consumed: 450 
Consumer Type (Residential/Commercial): Commercial 
Senior Citizen (Y/N): Y 
----------------------------------------------------------------------------------------------------------
Sample Output 
Base Bill: ₹4500 
Commercial Charge: ₹900 
Surcharge: ₹270 
Senior Citizen Discount: ₹567 
Final Bill Amount: ₹5103
---------------------------------------------------------------------------------------------------------
'''

#--------------------------------------------------------------------------------------------------------
#----------------------------------------------Coding----------------------------------------------------

# Taking Units consumed input from the user
units = int(input("Enter Units Consumed : "))

# Taking consumer type input from the user
consumer_type = input("Enter Consumer Type (Residential/Commercial) : ")

# Taking senior citizen input from the user
senior_citizen = input("Senior Citizen (Y/N) : ")

print("-------------------------------------------------------------------------------------------------")

#-----------------------------------------------------------------------------------------------------------

# validating units consumed

if (units <= 0):
    exit("Units Consumed must be positive")

#------------------------------------------------------------------------------------------------------------

# calculating unit consumed
base_bill = 0
if (units <= 100):
    base_bill = units * 5
    print("Base Bill : " , base_bill)
elif(units >= 101 and units <= 300):
    base_bill = units * 7
    print("Base Bill : " , base_bill)
else:
    base_bill = units * 10
    print("Base Bill : " , base_bill)

#----------------------------------------------------------------------------------------------------------------

# checking whether the consumer is commercial or not
# Commercial consumers pay 20% extra

commerical_charge = 0
if (consumer_type == 'Commercial'):
    commerical_charge = base_bill * 0.20
    print("Commerical Charge : " , commerical_charge)


#-------------------------------------------------------------------------------------------------------------

# checking whether the Bill is above 5000
# Bills above ₹5000 attract 5% surcharge

combine = base_bill + commerical_charge
subcharge = 0
if (combine > 5000):
    subcharge =  combine* 0.05
    print("Subcharge : " ,subcharge)

#-----------------------------------------------------------------------------------------------------------

# checking if the citizen is senior citizen or not
# Senior citizens receive 10% discount.  

discount = 0
total = base_bill + commerical_charge + subcharge
if (senior_citizen == 'Y'):
    discount = total * 0.10
    print("Senior Citizen Discount : " , discount)

#----------------------------------------------------------------------------------------------------------------

# Final bill price
print("Final Bill Price : " ,(base_bill+commerical_charge+ subcharge - discount))

#----------------------------------------------------------------------------------------------------------------

'''Output:
Enter Units Consumed : 200
Enter Consumer Type (Residential/Commercial) : Commercial 
Senior Citizen (Y/N) : N
---------------------------------------------------------------------------------------
Base Bill :  1400
Commerical Charge :  280.0
Final Bill Price :  1680.0
-----------------------------------------------------------------------------------------
'''



