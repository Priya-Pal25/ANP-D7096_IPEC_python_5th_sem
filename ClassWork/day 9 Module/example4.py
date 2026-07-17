# importing module
import numericcalculation as nc

#-----------------------------------------------------------------------------------------------

a = 5
b = 10

# addition
print("Sum of",a ,"and",b,"is : " , nc.calculate_addition(a,b))
#-----------------------------------------------------------------------------------------------

m = 50
n = 40

# difference
print("Difference of " , a, "and" , b,"is : ",nc.calculate_difference(m,n))

#------------------------------------------------------------------------------------------------

# multiplication
print("Multiplication of ",m,"and",n,"is : ",nc.calculate_multiplication(m,n))
#------------------------------------------------------------------------------------------------

# division
print("Division of ",m,"and",n,"is : ",nc.calculate_division(m,n))
#-------------------------------------------------------------------------------------------------

# remainder
print("Remainder of ",m,"and",n,"is : ",nc.calculate_remainder(m,n))