'''Program to create a tuple of 15 numbers given by user and 
display the odd numbers present in that tuple'''

# creating a blank list
number_list=[]
print("Enter any 15 numbers: ")

for x in range(15):
    # input from the user
    num = int(input())
    # inserting into the list
    number_list.append(num)

#---------------------------------------------------------
# converting the list into tuple

numbers = tuple(number_list)
print("--------------------------------------------------")
print("Tuple of 15 numbers:")
print(numbers)

# display odd numbers
print("The odd number in the tuple")
for element in numbers:
    if (element % 2 == 1):
        print(element,end = ',')

#--------------------------------------------------------------------

'''Output:
Enter any 15 numbers: 
21
34
56
76
45
34
89
31
23
52
11
14
16
17
24
--------------------------------------------------
Tuple of 15 numbers:
(21, 34, 56, 76, 45, 34, 89, 31, 23, 52, 11, 14, 16, 17, 24)
The odd number in the tuple
21,45,89,31,23,11,17,
'''