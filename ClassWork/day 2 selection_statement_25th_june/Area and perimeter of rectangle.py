'''Write a program to calculate area and perimeter of rectangle and validate it'''

#input from the user

length = float(input("Enter the Length of the recatangle: "))
#validating the length of recatangle
if length < 0:
    exit("length cannot be negative.")
#validating the breadth of rectangle
breadth = float(input("Enter the breath of the rectangle: "))
if breadth < 0:
    exit("breadth cannot be negative.")
#--------------------------------------------------------------------

#displaying the data to the user

print("length of the recatngle: ",length)
print("Breadth of the rectangle: ",breadth)
#-------------------------------------------------------------------------

# displaying perimeter of recatngle

print("The perimeter of rectangle is : ",(2*(length + breadth )))

#displaying Area of ractangle

print("The Area of the reactangle is : ",(length * breadth))
#----------------------------------------------------------------------------

'''Output:
Enter the Length of the recatangle: 5.0
Enter the breath of the rectangle: 6.0
length of the recatngle:  5.0
Breadth of the rectangle:  6.0
The perimeter of rectangle is :  22.0
The Area of the reactangle is :  30.0'''

