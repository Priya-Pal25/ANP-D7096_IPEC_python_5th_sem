''' ----------------------------------Airline Ticket Pricing Engine ----------------------------------------

An airline calculates ticket fare using: 
Base Fare = ₹5000 
Additional Charges: 
• Business Class → +₹3000  
• Window Seat → +₹500  
• Weekend Travel → +₹1000  
--------------------------------------------------------------------------------------------------------
Discounts: 
• Age below 12 → 50%  
• Age above 60 → 20%  
Calculate the final ticket fare. 
---------------------------------------------------------------------------------------------------------
Sample Input 
Enter Passenger Age: 65 
Business Class (Y/N): Y 
Window Seat (Y/N): Y 
Weekend Travel (Y/N): Y 
---------------------------------------------------------------------------------------------------------
Sample Output 
Base Fare: ₹5000 
Additional Charges: ₹4500 
Senior Citizen Discount: 20% 
Final Ticket Fare: ₹7600.0 
----------------------------------------------------------------------------------------------------------
'''

#----------------------------------------------------------------------------------------------------------
#----------------------------------------Coding------------------------------------------------------------

# Taking age input from user
age = int(input("Enter Passenger Age (in years) : " ))

# Taking business class input from user
business_class =input("Business Class (Y/N) : " )

# Taking window seat input from the user
window_seat = input("Window Seat (Y/N) : " )
# Taking weekend travel input from the user
weekend_travel = input("Weekend Travel (Y/N) : " )

print("----------------------------------------------------------------------------------------------------")

#------------------------------------------------------------------------------------------------------------

# validating age
if (age <=0):
    exit("Age must be positive")

#-------------------------------------------------------------------------------------------------------------

# calculating additional charges

base_fare = 5000
print("Base Fare:",base_fare)
charge = 0
if (business_class == "Y"):
    charge = charge + 3000
if(window_seat == "Y"):
    charge=charge + 500

if (weekend_travel == "Y"):
    charge = charge+ 1000

print("Additional Charge : ",charge)

#--------------------------------------------------------------------------------------------------------------

# verifying discount applicable or not

total = base_fare + charge
if (age <12):
    print("Child discount : 50 %")
    print("Final Ticket Fare: " ,(total - (total * 0.50) ))

elif (age > 60 ):
    print("Senior citizen discount : 20% ")
    print("Final Ticket Fare: " , (total - (total * 0.20)))
else:
    print("No discount")
    print("Final Ticket Fare: " , total)

#----------------------------------------------------------------------------------------------------------------


'''Output:
Enter Passenger Age (in years) : 20
Business Class (Y/N) : Y
Window Seat (Y/N) : Y
Weekend Travel (Y/N) : N
-----------------------------------------------------------------------------------------------------------------
Base Fare: 5000
Additional Charge :  3500
No discount
Final Ticket Fare:  8500
'''

