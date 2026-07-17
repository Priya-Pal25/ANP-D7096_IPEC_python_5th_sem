'''----------------------------Write a function to calculate simple interest------------------------------'''

# function to calaculate simple interest
def Calculate_Simple_Interest(principal,rate,time):
    return (principal * rate * time)

#------------------------------------------------------------------------------------------------------------
# main program

principal = float(input("Enter principal (in Rs): "))
rate = float(input("Enter rate (in %): "))
time = int(input("Enter time (in years) : "))

print("Simple Interest : " , Calculate_Simple_Interest(principal,rate,time))

#-----------------------------------------------------------------------------------------------------

'''Output:
Enter principal (in Rs): 2000
Enter rate (in %): 2.5
Enter time (in years) : 2
Simple Interest :  10000.0
'''
