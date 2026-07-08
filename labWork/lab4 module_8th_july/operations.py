# importing twodfigures
from twodfigures import *

#-------------------------------------------------------------------------------------------------------
# displaying menu
while True:
    print("------------------------------------------FIGURES-----------------------------------------")
    print("Square")
    print("Circle")
    print("Triangle")
    print("Rectangle")
    print("Exit")

    print("-----------------------------------------------------------------------------------------------")
    choice = input("Enter choice : ")

#--------------------------------------------------------------------------------------------------------------------
# for square opertions

    if (choice == 'Square' or choice == 'square'):
        side = float(input("Enter the side of a square : "))
        print("-----------------------------------------Operations-----------------------------------------------")
        print("Area")
        print("Perimeter")
        ch = input("Enter choice : ")
        if (ch == 'Area' or ch == 'area'):
            print("Area of the square is : " , calculate_square_area(side))
        elif (ch == 'Perimeter' or ch == 'perimeter'):
            print("Perimeter of the square is : ", calculate_square_perimeter(side))
        else:
            print("Invalid choice")

#---------------------------------------------------------------------------------------------------------------------
# for circle operations

    elif (choice == 'Circle' or choice == 'circle'):
        radius = float(input("Enter the radius of a circle : "))
        print("--------------------------------------------Operations---------------------------------------------")
        print("Area")
        print("Perimeter")
        ch = input("Enter choice : ")
        if (ch == 'Area' or ch == 'area'):
            print("Area of the circle is : " ,calculate_circle_area(radius))
        elif (ch == 'Perimeter' or ch == 'perimeter'):
            print("Perimeter of the circle is : " , calculate_circle_perimeter(radius))
        else:
            print("Invalid choice")

#---------------------------------------------------------------------------------------------------------------------------
# for triangle operations

    elif (choice == 'Triangle' or choice == 'triangle'):
        side = float(input("Enter the side of the triangle : "))
        base = float(input("Enter the base of the triangle : "))
        height = float(input("Enter the height of the triangle : "))
        print("----------------------------------Operations----------------------------------------------")
        print("Area")
        print("Perimeter")
        ch = input("Enter the choice : ")
        if (ch == 'Area' or ch == 'area'):
            print("Area of the triangle is : ",calculate_triangle_area(base,height))
        elif (ch == 'Perimeter' or ch == 'perimeter'):
           
            print("Perimeter of the triangle is : ",calcualte_triangle_perimeter(side,base,height))
        else:
            print("Invalid choice")

#-----------------------------------------------------------------------------------------------------------------------
# for rectangle operations

    elif (choice == 'Rectangle' or choice == 'rectangle'):
        length = float(input("Enter the length of the rectangle : "))
        breadth = float(input("Enter the breadth of the rectangle : "))
        print("------------------------------------Operations-----------------------------------------------")
        print("Area")
        print("Perimeter")
        ch = input("Enter the choice : ")
        if (ch == 'Area' or ch == 'area'):
            print("Area of the rectangle is : ",calculate_rectangle_area(length,breadth))
        elif (ch == 'Perimeter' or ch == 'perimeter'):
            print("Perimeter of the rectangle is : " ,calculate_rectangle_perimeter(length,breadth))
        else:
            print("Invalid choice")
    
    elif (choice == 'Exit ' or choice == 'exit'):
        break
    else:
        print("Invalid choice")

#----------------------------------------------------------------------------------------------------------------------------------

'''Output:
------------------------------------------FIGURES-----------------------------------------
Square
Circle
Triangle
Rectangle
Exit
-----------------------------------------------------------------------------------------------
Enter choice : Square
Enter the side of a square : 4
-----------------------------------------Operations-----------------------------------------------
Area
Perimeter
Enter choice : Area
Area of the square is :  16.0
------------------------------------------FIGURES-----------------------------------------
Square
Circle
Triangle
Rectangle
Exit
-----------------------------------------------------------------------------------------------
Enter choice : Exit
'''