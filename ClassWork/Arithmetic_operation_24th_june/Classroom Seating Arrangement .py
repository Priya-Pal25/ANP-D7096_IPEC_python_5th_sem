"""Write a Python program to determine how many complete rows can be formed."""

Total_Student = int(input("Enter the Total Students : " ))
Student_per_row = int(input("Enter the number of Student per rows : " ))

print("Number of Complete Rows : " , (Total_Student / Student_per_row))