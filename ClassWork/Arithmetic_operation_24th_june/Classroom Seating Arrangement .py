'''Write a Python program to determine how many complete rows can be formed.'''
#taking input from the user

Total_Student = int(input("Enter the Total Students : " ))
Student_per_row = int(input("Enter the number of Student per rows : " ))
#------------------------------------------------------------------------------------------

#displaying the input to the user
print("Total Students : ",Total_Student)
print("Student per Row : ",Student_per_row)
#-------------------------------------------------------------------------------------------

#displaying the Number of complete Rows

print("Number of Complete Rows : " , (Total_Student / Student_per_row))
#--------------------------------------------------------------------------------------------
'''Output :
Enter the Total Students : 60
Enter the number of Student per rows : 5
Total Students :  60
Student per Row :  5
Number of Complete Rows :  12.0'''