'''--------Program to display elements placed at odd position--------------------'''

# creating a list

numbers = [40,90,23,87,91,45,68,24,84]
print("list are : ")
print(numbers)

print("--------------------------------------------------------")

print("Elements at odd position:")

for x in range(0,len(numbers),2):
    print(numbers[x],end = ',')
    
#------------------------------------------------------------------

'''Output:
list are : 
[40, 90, 23, 87, 91, 45, 68, 24, 84]
--------------------------------------------------------
Elements at odd position:
40,23,91,68,84,
'''
