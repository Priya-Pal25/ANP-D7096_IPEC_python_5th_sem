'''Write a Python program to find the average mileage of a car.'''

# Taking input from the user

Total_distance_traveled = float(input("Enter the Total distance traveled (in km): " ))
Fuel_consumed = float(input("Enter fuel comsumed (in liters): " ))
#------------------------------------------------------------------------------------------------------

# Displaying the input to the user
print("Total Distance Traveled (in Km): " ,Total_distance_traveled)
print("Fuel  Consumed (in liters): " ,Fuel_consumed)
#--------------------------------------------------------------------------------------------------------

# Displaying the Mileage to the user

print("Mileage : " , (Total_distance_traveled / Fuel_consumed))
#---------------------------------------------------------------------------------------------------------
'''Output:
Enter the Total distance traveled (in km): 2500.0
Enter fuel comsumed (in liters): 50.0
Total Distance Traveled (in Km):  2500.0
Fuel  Consumed (in liters):  50.0
Mileage :  50.0
'''