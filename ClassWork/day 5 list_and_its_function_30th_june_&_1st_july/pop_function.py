''' Write a program to take input of 10 number as a list and 
take index from the user to delete the element at the specified index'''

# creating list
list=[]
print("The 10 numbers are:")

#-----------------------------------------------------------------------------------

# taking 10 numbers from the user 
for x in range(10):
    num = int(input())
    list.append(num)

print("---------------------------------------------------------------------------")
print("Numbers are : ",list)

# taking index input from the user
index = int(input("Enter the index you want to delete: "))

# deleting element from the list at specified position
list.pop(index)

# displaying updated list
print("New list is :",list)

'''Output:
The 10 numbers are:
23
12
43
54
67
86
21
1
2
4
--------------------------------------------------------------------
Numbers are :  [23, 12, 43, 54, 67, 86, 21, 1, 2, 4]
Enter the index you want to delete: 3
New list is : [23, 12, 43, 67, 86, 21, 1, 2, 4]
'''