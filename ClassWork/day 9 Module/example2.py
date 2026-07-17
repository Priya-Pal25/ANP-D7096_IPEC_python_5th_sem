# importing module
from numericcalculation import *

#-----------------------------------------------------------------------------------------------

a = 4
b = 2

# addition
print("Sum of",a ,"and",b,"is : " , calculate_addition(a,b))
#-----------------------------------------------------------------------------------------------

# difference
print("Difference of " , a, "and" , b,"is : ", calculate_difference(a,b))

#------------------------------------------------------------------------------------------------

# multiplication
print("Multiplication of ",a,"and",b,"is : ",calculate_multiplication(a,b))
#------------------------------------------------------------------------------------------------

# division
print("Division of ",a ,"and",b,"is : ",calculate_division(a,b))
#-------------------------------------------------------------------------------------------------

# remainder
print("Remainder of ",a,"and",b,"is : ",calculate_remainder(a,b))

'''Output:
Sum of 4 and 2 is :  6
Difference of  4 and 2 is :  2
Multiplication of  4 and 2 is :  8
Division of  4 and 2 is :  2.0
Remainder of  4 and 2 is :  0
'''