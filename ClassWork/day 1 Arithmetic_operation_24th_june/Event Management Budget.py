'''Write a Python program to calculate how much each participant should pay. '''
#takng input from user

cost = float(input("Enter the Total Event Cost (in Rs): "))
participants = int(input("Enter the Number of participants : "))

#----------------------------------------------------------------------------------------

#display the input to the user
print("Total Event Cost (in Rs): " ,cost)
print("Number of Participant : ",participants)

#----------------------------------------------------------------------------------------

#displaying Amount per participants

print("Amount per Participant : ",(cost / participants))
#---------------------------------------------------------------------------------------
'''Output:
Enter the Total Event Cost (in Rs): 500.0
Enter the Number of participants : 10
Total Event Cost (in Rs):  500.0
Number of Participant :  10
Amount per Participant :  50.0
'''