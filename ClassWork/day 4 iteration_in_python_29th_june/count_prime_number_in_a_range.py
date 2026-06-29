''' ---------------------------------------------------Count Prime Numbers in a Range -------------------------------------------

Accept two integers representing the starting and ending values of a range. 
Display all prime numbers within the range and
finally display the total number of prime numbers 
found. 
--------------------------------------------------------------------------------------------------------------------------------
'''

#------------------------------------------------------------------------------------------------------------------------------

# Taking first number input from the user

num1 = int(input("Enter first number : "))

# Taking second number input from the user

num2 = int(input("Enter second Number: "))

#-------------------------------------------------------------------------------------------------------------------------------


# Validating numbers
if num1 < 0 or num2 < 0:
    exit("Numbers must be positive")

count = 0

print("Prime numbers are:")

for i in range(num1, num2 + 1):

    if i < 2:
        continue

    prime = True

    for j in range(2, i):
        if i % j == 0:
            prime = False
            break

    if prime:
        print(i)
        count += 1

print("Total Prime Numbers:", count)


#------------------------------------------------------------------------------------------------------------------------------------
'''Output:
Enter first number : 1
Enter second Number: 10
Prime numbers are:
2
3
5
7
Total Prime Numbers: 4
'''