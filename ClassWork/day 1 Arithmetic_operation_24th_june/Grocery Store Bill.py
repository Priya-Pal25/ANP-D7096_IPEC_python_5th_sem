'''Write a Python program to calculate the total cost of rice packets purchased. '''
# Taking the input from the user

Price = float(input("Enter the Price per packet (in Rs): "))
Number_of_Packets = int(input("Enter the number of packets: "))
#----------------------------------------------------------------------------------------------------

# Displaying the input to the user 
print("Price per packet (in Rs): " ,Price)
print("Number of packets : " ,Number_of_Packets)

#-----------------------------------------------------------------------------------------------------

# Displaying the Total Bill Amount
print("Total Bill Amount : ",(Price * Number_of_Packets))

#-----------------------------------------------------------------------------------------------------
'''Output:
Enter the Price per packet (in Rs): 500.0
Enter the number of packets: 5
Price per packet (in Rs):  500.0
Number of packets :  5
Total Bill Amount :  2500.0
'''
