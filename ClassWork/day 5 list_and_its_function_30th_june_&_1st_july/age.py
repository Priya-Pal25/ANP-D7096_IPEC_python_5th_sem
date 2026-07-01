'''Write a program to input the age of 15 person
and display the total no. of person as adult whose age is >=18'''

# creating list

list=[]
print("Enter the age of 15 person: ")

# taking input from user
for x in range(15):
    person = int(input())
    list.append(person)

print("----------------------------------------------------------------")
print("The age are : ",list)

#-----------------------------------------------------------------------------
print("Person's who are adults : ")
for x in list:
    if ( x >= 18):
        print(x,end = ',')

#------------------------------------------------------------------------------

'''Output:
Enter the age of 15 person: 
12
34
15
16
56
34
24
56
78
32
54
37
89
32
21
----------------------------------------------------------------
The age are :  [12, 34, 15, 16, 56, 34, 24, 56, 78, 32, 54, 37, 89, 32, 21]
Person's who are adults : 
34,56,34,24,56,78,32,54,37,89,32,21,
'''

