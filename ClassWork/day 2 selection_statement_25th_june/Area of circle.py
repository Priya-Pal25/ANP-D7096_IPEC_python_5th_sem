''' Write a program to calculate area of circle and validate it'''

#input of radius from the user
radius = float(input("Enter the radius of circle : "))
#validating the radius of circle
if radius < 0:
    exit("Radius of the circle cannot be negative.")
#--------------------------------------------------------------

#displaying the input to the user

print("Radius of circle is : ",radius)
#--------------------------------------------------------------

#displaying area of circle

print("Area of circle is : " ,(3.14 * radius * radius))
#-----------------------------------------------------------

''' Output:
Enter the radius of circle : 25.0
Radius of circle is :  25.0
Area of circle is :  1962.5
'''