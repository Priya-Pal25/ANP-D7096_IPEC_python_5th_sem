'''write a program to calculate compound interest'''


#taking input from user
principal = float(input("Enter the principal (in Rs) :"))
#validating the principal
if principal <0:
    exit("Principal cannot be negative")
rate = float(input("Enter the rate of interest (in %) :"))
#validating the rate
if rate < 0:
    exit("Rate cannot be negative")
time = int(input("Enter the time period (in years): "))
#validating the time
if time < 0:
    exit("Rate cannot be negative")
#-------------------------------------------------------------------------------

#displaying the input

print("Principal (in Rs): ",principal)
print("Rate (in %) : ",rate)
print("Time (in years) :",time)
#-------------------------------------------------------------------------------

#calculate compound interest
print("Compound interest :",(principal*((1+rate)**time)))
#-------------------------------------------------------------------------------
'''Output:
nter the principal (in Rs) :50000
Enter the rate of interest (in %) :2.5
Enter the time period (in years): 2
Principal (in Rs):  50000.0
Rate (in %) :  2.5
Time (in years) : 2
Compound interest : 612500.0    

'''
