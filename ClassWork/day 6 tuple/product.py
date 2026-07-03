'''program to create a tuple of prices of 10 products.display the lowest price,highest price
and count the no of product where price is greater than 4000
along with the price you are required to store the name of the prooduct also and
while displaying the lowest price and highest price display the name of the product also
'''

# creating a tuple

products =( ('fan',2000),('pen',50),('phone',10000),('ring',500),('charger',2000),('bottle',2000),('mouse',4500),('keyboard',6000),('shoes',3500),('table',4000))

#----------------------------------------------------------------------------------------------------------
lowest = products[0][1]
highest = products[0][1]
count = 0
index_max = 0
index_min = 0
for x in range(10):
    # calculating highest price product
    if (products[x][1] > highest):
        highest = products[x][1]
        index_max = x

    # calculating lowest price product
    if (products[x][1] < lowest):
        lowest = products[x][1]
        index_min = x
    
    # count the number of product price greater than 4000
    if (products[x][1] > 4000):
            count = count +1

#--------------------------------------------------------------------------------------------

# displaying the highest price along with the name
print("The Highest price Product name : ",products[index_max][0],"and Price : ",highest)

# displaying the lowest price along with the name
print("The lowest price Product name : ",products[index_min][0],"and Price : ",lowest) 

# count the number of product greater than 4000
print("freq of products price greater than 4000: ",count)

#--------------------------------------------------------------------------------------------------

'''Output:
The Highest price Product name :  phone and Price :  10000
The lowest price Product name :  pen and Price :  50
freq of products price greater than 4000:  3
'''