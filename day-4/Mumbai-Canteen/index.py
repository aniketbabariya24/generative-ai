inventory = {
    1: {'name': 'Chips', 'price': 10, 'availability': 'yes'},
    2: {'name': 'Biscuits', 'price': 5, 'availability': 'yes'},
    3: {'name': 'Chocolate', 'price': 20, 'availability': 'yes'}
}

def displayInventory():
    print("Snack Inventory:")
    for snackId, snack in inventory.items():
        print(f"ID: {snackId}, Name: {snack['name']}, Price: {snack['price']}, Availability: {snack['availability']}")

def addSnack():
    print("Adding a new snack to the inventory:")
    snackId = int(input("Enter snack ID: "))
    name = input("Enter snack name: ")
    price = float(input("Enter snack price: "))
    availability = input("Is the snack available? (yes/no): ")
    
    inventory[snackId] = {'name': name, 'price': price, 'availability': availability}
    print("Snack added successfully!")

def removeSnack():
    print("Removing a snack from the inventory:")
    snackId = int(input("Enter snack ID: "))
    
    if snackId in inventory:
        del inventory[snackId]
        print("Snack removed successfully!")
    else:
        print("Snack not found in the inventory.")

def updateAvailability():
    print("Updating snack availability:")
    snackId = int(input("Enter snack ID: "))
    
    if snackId in inventory:
        availability = input("Is the snack available? (yes/no): ")
        inventory[snackId]['availability'] = availability
        print("Snack availability updated successfully!")
    else:
        print("Snack not found in the inventory.")

def recordSale():
    print("Recording a snack sale:")
    snackId = int(input("Enter snack ID: "))
    
    if snackId in inventory:
        if inventory[snackId]['availability'] == 'yes':
            inventory[snackId]['availability'] = 'no'
            print("Snack sale recorded successfully!")
        else:
            print("Snack is not available for sale.")
    else:
        print("Snack not found in the inventory.")


while True:
    print("\nCanteen Management System\n")
    print("1. Display inventory")
    print("2. Add a snack to the inventory")
    print("3. Remove a snack from the inventory")
    print("4. Update snack availability")
    print("5. Record a snack sale")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        displayInventory()
    elif choice == '2':
        addSnack()
    elif choice == '3':
        removeSnack()
    elif choice == '4':
        updateAvailability()
    elif choice == '5':
        recordSale()
    elif choice == '6':
        print("Thank you for using the Canteen Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
