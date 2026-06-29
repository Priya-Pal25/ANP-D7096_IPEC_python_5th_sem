'''------------------------------------------Shopping Cart Billing System------------------------------------------------------------ 

A supermarket allows a customer to purchase multiple products. 
The customer first enters the number of products. 
For each product, enter: 
• Product Name  
• Quantity  
• Price per Unit  
Finally display: 
• Individual Product Cost  
• Total Bill Amount  
• Most Expensive Product  
• Cheapest Product  
• Average Product Cost
------------------------------------------------------------------------------------------------------------------------------------
'''
#----------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------Coding-----------------------------------------------------------------

# Taking input from the user
products = int(input("Enter the number of products: "))

# Validate the number of products
if products <= 0:
    exit("Number of products must be positive")

#----------------------------------------------------------------------------------------------------------------------


total_bill = 0

max_cost = 0
min_cost = 0

max_product = ""
min_product = ""

# Accept details of each product
for x in range(1, products + 1):

    print("Product", x)

    # Taking product details
    product_name = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price per Unit: "))

    # Calculate product cost
    cost = quantity * price

    # Display individual product cost
    print("Product Cost:", cost)

    # Add to total bill
    total_bill = total_bill + cost


    if x == 1:
        max_cost = cost
        min_cost = cost
        max_product = product_name
        min_product = product_name

    # Find most expensive product
    if cost > max_cost:
        max_cost = cost
        max_product = product_name

    # Find cheapest product
    if cost < min_cost:
        min_cost = cost
        min_product = product_name

#-----------------------------------------------------------------------------------------------------------------------------------------


# Display the final results

print("Total Bill Amount:", total_bill)
print("Most Expensive Product:", max_product, ":", max_cost)
print("Cheapest Product:", min_product, ":", min_cost)
print("Average Product Cost:", (total_bill / products))

#----------------------------------------------------------------------------------------------------------------------------------
'''Output:
Enter the number of products: 3
Product 1
Enter Product Name: milk
Enter Quantity: 2
Enter Price per Unit: 80
Product Cost: 160.0
Product 2
Enter Product Name: chips
Enter Quantity: 2
Enter Price per Unit: 10
Product Cost: 20.0
Product 3
Enter Product Name: chocolate
Enter Quantity: 2
Enter Price per Unit: 20
Product Cost: 40.0
Total Bill Amount: 220.0
Most Expensive Product: milk : 160.0
Cheapest Product: chips : 20.0
Average Product Cost: 73.33333333333333
'''