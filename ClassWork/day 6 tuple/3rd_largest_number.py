'''Program to find 3rd largest number from a list of 20 number given by user'''

# creating a blank list
numbers = []

print("Enter any 20 numbers:")
for x in range(20):
    # taking number from user
    num = int(input())
    # appending number into the list
    numbers.append(num)

print("The list of 20 numbers :")
print(numbers)
print("---------------------------------------------------------------------")

# sori+ting the list in reverse order
numbers.sort(reverse=True)

print("The third largest number : ",numbers[2])
#--------------------------------------------------------------------------

'''Output:
Enter any 20 numbers:
56
32
14
52
12
14
16
17
19
43
42
46
28
20
60
98
57
11
1
73
The list of 20 numbers :
[56, 32, 14, 52, 12, 14, 16, 17, 19, 43, 42, 46, 28, 20, 60, 98, 57, 11, 1, 73]
---------------------------------------------------------------------
The third largest number :  60
'''
