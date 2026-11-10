# Question 2 - Arrays and Loops
# Topic: Inventory Tracker
#
# Task 1:
# Declare an empty list called inventory to store item names as strings.

# Add your code here
# Task 1: Declare an empty list called inventory
inventory = []

# Task 2:
# Write a function called addItem(itemName) that adds the given item to the
# inventory list. If the item already exists, print a message instead of adding it.
# Example message: "Mouse is already in inventory."

def addItem(itemName):
    # Check if the item is already present in the inventory list
    if itemName in inventory:
        print(f"{itemName} is already in inventory.")
    else:
        # Add the new item to the list
        inventory.append(itemName)
    


# Task 3:
# Write a function called listInventory() that prints all items in the inventory.
# If the inventory is empty, print: "Inventory is empty."

def listInventory():
    # Check whether the inventory list contains any items
    if not inventory:
        print("Inventory is empty.")
    else:
        # Print the current list of inventory items
        print(f"Inventory: {inventory}")
    


# Task 4:
# Call the functions in this order and observe the output:
addItem("Laptop")
addItem("Mouse")
addItem("Keyboard")
addItem("Mouse")   # Should trigger duplicate warning
listInventory()

# Expected output:
# Mouse is already in inventory.
# Inventory: ['Laptop', 'Mouse', 'Keyboard']
