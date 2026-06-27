'''Write a Python program to find how many slices remain after equal distribution.'''

# Taking input from the user 

slices = int(input("Enter the Total Pizza Slices : " ))
Number_of_children = int(input("Enter the Number of Student : " ))
#-------------------------------------------------------------------------------------------------

# Displaying the input to the user

print("Total Pizza Slices : " ,slices)
print("Number of Children : " ,Number_of_children)
#-------------------------------------------------------------------------------------------------

# Displaying Remaining Slices

print("Remaining Slices : " , (slices - Number_of_children))
#-------------------------------------------------------------------------------------------------
'''Output:
Enter the Total Pizza Slices : 8
Enter the Number of Student : 4
Total Pizza Slices :  8
Number of Children :  4
Remaining Slices :  4
'''
