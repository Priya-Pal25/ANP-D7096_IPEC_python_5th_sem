''' --------------------------------Courier Delivery Charge--------------------------------------------- 

A courier company calculates delivery charges based on the package weight. 
• Weight up to 2 kg → ₹50  
• Weight greater than 2 kg and up to 5 kg → ₹100  
• Weight greater than 5 kg → ₹180  
Write a Python program to display the delivery charge. 
------------------------------------------------------------------------------------------------------
Sample Input 
4 
------------------------------------------------------------------------------------------------------
Sample Output 
Delivery Charge = ₹100
------------------------------------------------------------------------------------------------------
'''

#-----------------------------------------------------------------------------------------------------
#---------------------------------------------------Coding-------------------------------------------

# Taking package weight input from the user

package_weight = float(input("Enter the Package weight (in kg): "))

print("-----------------------------------------------------------")

#---------------------------------------------------------------------------------------------------

# Validating package weight

if (package_weight <= 0):
    exit("Package Weight must be positive")

#------------------------------------------------------------------------------------------------------

# Calculating delivery charges

if (package_weight <= 2):
    print("Delivery Charge : 50")
elif (package_weight > 2 and package_weight <= 5):
    print("Delivery Charges : 100")
else:
    print("Delivery Charges : 180")

#--------------------------------------------------------------------------------------------------------

'''Output:
Enter the Package weight (in kg): 7
-----------------------------------------------------------
Delivery Charges : 180
'''