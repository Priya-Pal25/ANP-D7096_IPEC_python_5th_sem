'''---------------------------------------Internet Speed Rating --------------------------------------------- 
 
An Internet Service Provider categorizes connection quality based on download speed. 
• Less than 25 Mbps → Slow  
• 25 - 99 Mbps → Good  
• 100 Mbps or above → Excellent  
Write a Python program to display the connection quality. 
------------------------------------------------------------------------------------------------------------
Sample Input 
120 
-------------------------------------------------------------------------------------------------------------
Sample Output 
Excellent Connection 
-------------------------------------------------------------------------------------------------------------
'''

#-----------------------------------------------------------------------------------------------------------
#---------------------------------------Coding-------------------------------------------------------------

# Taking connection quality input from the user

download_speed = int(input("Enter download speed : "))

print("-----------------------------------------------------------------------------")

#--------------------------------------------------------------------------------------

# Validate doenload speed
if (download_speed <= 0):
    exit("Invalid Input! Download speed must be positive")

#-------------------------------------------------------------------------------------

# displaying connection quality

if (download_speed < 25):
    print("Slow Connection")
elif (download_speed >= 25 and download_speed <= 99):
    print("Good Connection")
else:
    print("Excellent Connection")

#-------------------------------------------------------------------------------------

'''Output:
Enter download speed : 45
-----------------------------------------------------------------------------
Good Connection
'''