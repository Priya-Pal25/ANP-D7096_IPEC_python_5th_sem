# craeting list
numbers = []
print("Enter the numbers :")

# taking input from user
for x in range(20):
    num = int(input())
    numbers.append(num)

print("list is : ",numbers)


# taking a num input from the user to delete the occurrence of element more than 1
element = int(input("Enter the number :"))


freq = numbers.count(element)

if freq == 0:
    print(element,"not found")

elif freq == 1:
    print("no duplicate found")
else:
    numbers.reverse()
    for x in range(1,freq):
        numbers.remove(element)
    numbers.reverse()
    print("list after removing the duplicate occurence: ",numbers)


'''Output:
Enter the numbers :
2
3
4
1
5
6
3
2
1
4
5
7
8
4
3
6
2
1
3
4
list is :  [2, 3, 4, 1, 5, 6, 3, 2, 1, 4, 5, 7, 8, 4, 3, 6, 2, 1, 3, 4]
Enter the number :1
list after removing the duplicate occurence:  [2, 3, 4, 1, 5, 6, 3, 2, 4, 5, 7, 8, 4, 3, 6, 2, 3, 4]
'''
