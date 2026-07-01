'''Write a program to input the age of 10 person from the user
and count how many people are eligible for voting(age 18 or above).
display the total number of eligible people'''

# creating list

list=[]
print("Enter the age of 10 person: ")

# taking input from user
for x in range(10):
    person = int(input())
    list.append(person)

print("----------------------------------------------------------------")
print("The age are : ",list)

#-----------------------------------------------------------------------------

# checking elgibility for voting
count = 0
for x in list:
    if ( x >= 18):
        count = count +1

# display total no of eligible people for voting
print("Total number of eligible people are : ",count)

#------------------------------------------------------------------------------
'''Output:
Enter the age of 10 person: 
23
45
67
35
21
18
9
13
52
62
----------------------------------------------------------------
The age are :  [23, 45, 67, 35, 21, 18, 9, 13, 52, 62]
Total number of eligible people are :  8
'''