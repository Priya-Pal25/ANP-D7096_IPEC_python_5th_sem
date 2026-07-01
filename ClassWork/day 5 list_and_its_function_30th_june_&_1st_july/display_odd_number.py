'''Program to input 10 numbers and 
display odd numbers among them.'''

# creating list
numbers = []
print("Enter 10 numbers :")

# taking input from user
for x in range(10):
    num = int(input())
    numbers.append(num)

print("-----------------------------------------------")
print("Number are : ",numbers)
#---------------------------------------------------------------

# displaying odd numbers
print("odd no : ")
for x in numbers:
    if (x % 2 != 0):
        print(x,end = ',')


#------------------------------------------------------------------

'''Output:
Enter 10 numbers :
21
11
32
41
43
57
64
89
54
35
-----------------------------------------------
Number are :  [21, 11, 32, 41, 43, 57, 64, 89, 54, 35]
odd no : 
21,11,41,43,57,89,35,

'''
