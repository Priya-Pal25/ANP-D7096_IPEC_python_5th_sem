'''Write a Python program to calculate how much each participant should pay. '''

cost = float(input("Enter the Total Event Cost : "))
participants = int(input("Enter the Number of participants : "))

print("Amount per Participant : ",(cost / participants))