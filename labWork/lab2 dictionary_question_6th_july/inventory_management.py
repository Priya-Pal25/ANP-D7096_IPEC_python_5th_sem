'''------------------------------------Inventory Management------------------------------------
Create a dictionary to maintain the stock of products in a shop. 
Example: 
{ 
'Laptop': 15, 
'Mouse': 40, 
'Keyboard': 25, 
'Monitor': 10 
} 
Implement the following: 
• Add a new product.  
• Update the stock of an existing product.  
• Remove a product from inventory.  
• Display products having stock less than 20.  
• Display the total number of items available in the inventory. 
-----------------------------------------------------------------------------------------------'''

#------------------------------------------------------------------------------------------------
#--------------------------------------------------Coding----------------------------------------

# Create an empty dictionary
stock = {}

# Input products
n = int(input("Enter the number of products: "))

for i in range(n):
    product = input("Enter product name: ")
    quantity = int(input("Enter stock quantity: "))
    stock[product] = quantity

print("Inventory:")
print(stock)
print("------------------------------------------------------------------------------------")

#--------------------------------------------------------------------------------------------

# Add a new product
new_product = input("Enter new product name: ")
new_quantity = int(input("Enter stock quantity: "))
stock[new_product] = new_quantity

print("Inventory after adding a product:")
print(stock)
print("-----------------------------------------------------------------------------------")
#-------------------------------------------------------------------------------------------

# Update stock of an existing product
update_product = input("Enter product name to update: ")

if update_product in stock:
    new_stock = int(input("Enter new stock quantity: "))
    stock[update_product] = new_stock
    print("Stock updated successfully.")
else:
    print("Product not found.")

print("Inventory after updating:")
print(stock)
print("-----------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------

# Remove a product
remove_product = input("Enter product name to remove: ")

if remove_product in stock:
    del stock[remove_product]
    print("Product removed successfully.")
else:
    print("Product not found.")

print("Inventory after removing:")
print(stock)
print("--------------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------

# Display products having stock less than 20
print("Products having stock less than 20:")

for product in stock:
    if stock[product] < 20:
        print(product, ":", stock[product])

print("-------------------------------------------------------------------------------------------")
#--------------------------------------------------------------------------------------------------

# Display total number of items available
total = 0

for quantity in stock.values():
    total += quantity

print("Total number of items available:", total)

#---------------------------------------------------------------------------------------------------

'''Output:
Enter the number of products: 3
Enter product name: mouse
Enter stock quantity: 12
Enter product name: monitor
Enter stock quantity: 23
Enter product name: keyboard
Enter stock quantity: 21
Inventory:
{'mouse': 12, 'monitor': 23, 'keyboard': 21}
------------------------------------------------------------------------------------
Enter new product name: printer
Enter stock quantity: 15
Inventory after adding a product:
{'mouse': 12, 'monitor': 23, 'keyboard': 21, 'printer': 15}
-----------------------------------------------------------------------------------
Enter product name to update: keyboard
Enter new stock quantity: 25
Stock updated successfully.
Inventory after updating:
{'mouse': 12, 'monitor': 23, 'keyboard': 25, 'printer': 15}
-----------------------------------------------------------------------------------------
Enter product name to remove: monitor
Product removed successfully.
Inventory after removing:
{'mouse': 12, 'keyboard': 25, 'printer': 15}
--------------------------------------------------------------------------------------------
Products having stock less than 20:
mouse : 12
printer : 15
-------------------------------------------------------------------------------------------
Total number of items available: 52
'''