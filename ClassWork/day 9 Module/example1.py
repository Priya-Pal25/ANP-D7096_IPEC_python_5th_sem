# importing module
import numericcalculation

#-----------------------------------------------------------------------------------------------

a = 5
b = 10

# addition
print("Sum of",a ,"and",b,"is : " , numericcalculation.calculate_addition(a,b))
#-----------------------------------------------------------------------------------------------

# difference
print("Difference of " , a, "and" , b,"is : ", numericcalculation.calculate_difference(a,b))

#------------------------------------------------------------------------------------------------

# multiplication
print("Multiplication of ",a,"and",b,"is : ",numericcalculation.calculate_multiplication(a,b))
#------------------------------------------------------------------------------------------------

# division
print("Division of ",a ,"and",b,"is : ",numericcalculation.calculate_division(a,b))
#-------------------------------------------------------------------------------------------------

# remainder
print("Remainder of ",a,"and",b,"is : ",numericcalculation.calculate_remainder(a,b))

'''Output:
Sum of 5 and 10 is :  15
Difference of  5 and 10 is :  -5
Multiplication of  5 and 10 is :  50
Division of  5 and 10 is :  0.5
Remainder of  5 and 10 is :  5
'''