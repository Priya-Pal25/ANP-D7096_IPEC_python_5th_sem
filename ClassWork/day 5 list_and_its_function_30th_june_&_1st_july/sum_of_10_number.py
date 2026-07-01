'''-------------Program to find out sum of 10 numbers----------------'''

# creating list
numbers = []
print("Enter any 10 numbers:")

# taking input from user
for x in range(10):
    num = int(input())
    numbers.append(num)

#-------------------------------------------------------------------------

print("-----------------------------------------------------------------")
print("number are: ",numbers)

# finding sum
sum = 0
for x in numbers:
    sum= sum + x
print("Sum=",sum)

#--------------------------------------------------------------------------

'''Output:
nter any 10 numbers:
10
8
4
5
6
7
8
9
0
2
-----------------------------------------------------------------
number are:  [10, 8, 4, 5, 6, 7, 8, 9, 0, 2]
Sum= 59
'''