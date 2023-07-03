from tabulate import tabulate
import tkinter as tk
from tkinter import ttk, messagebox

menu = {}
orders = {}
wallet_amount=0
def displayMenu():
    print("==== Zomato Chronicles: The Great Food Fiasco ====")
    print("1. Show Menu")
    print("2. Add a new dish to the menu")
    print("3. Remove a dish from the menu")
    print("4. Update dish availability")
    print("5. Take a new order")
    print("6. Update order status")
    print("7. Review all orders")
    print("8. Exit")
    print("===================================================")
    pass

def addDish():
    dish_id = input("Enter the dish ID: ")
    dish_name = input("Enter the dish name: ")
    price = float(input("Enter the price: "))
    stocks = int(input("Enter the number of stocks: "))
    availability = input("Is the dish available? (yes/no): ")

    dish = {
        'dish_name': dish_name,
        'price': price,
        'stocks': stocks,
        'availability': availability.lower() == 'yes'
    }

    menu[dish_id] = dish
    print("Dish added successfully!")
    dish_added_label.config(text="Dish added successfully!")
    showMenu();

def removeDish():
    dish_id = input("Enter the dish ID to remove: ")

    if dish_id in menu:
        del menu[dish_id]
        print("Dish removed successfully!")
    else:
        print("Dish ID not found.")
    
    dish_removed_label.config(text="Dish removed successfully!")


def updateAvailability():
    dish_id = input("Enter the dish ID to update availability: ")

    if dish_id in menu:
        availability = input("Is the dish available? (yes/no): ")
        menu[dish_id]['availability'] = availability.lower() == 'yes'
        print("Availability updated successfully!")
    else:
        print("Dish ID not found.")

    availability_updated_label.config(text="Availability updated successfully!")
    


def takeOrders():
    customer_name = input("Enter customer name: ")
    order_items = input("Enter dish IDs (comma-separated): ").split(",")

    order = {
        'customer_name': customer_name,
        'order_items': [],
        'status': 'preparing'
    }

    for dish_id in order_items:
        if dish_id in menu:
            dish = menu[dish_id]
            quantity = int(input(f"Enter the quantity for {dish['dish_name']}: "))
            if quantity > dish['stocks']:
                print(f"Insufficient stocks for {dish['dish_name']}. Available stocks: {dish['stocks']}")
            else:
                order['order_items'].extend([dish_id] * quantity)
                dish['stocks'] -= quantity
                if dish['stocks'] == 0:
                    dish['availability'] = False
                print(f"{quantity} {dish['dish_name']} added to the order.")
        else:
            print("Invalid Dish ID:", dish_id)

    order_id = len(orders) + 1
    orders[order_id] = order

    print("Order placed successfully! Order ID:", order_id)
    order_placed_label.config(text="Order placed successfully! Order ID: {}".format(order_id))

    global wallet_amount
    total_price = sum(menu[dish_id]['price'] for dish_id in order['order_items'] if dish_id in menu)
    
    if total_price > wallet_amount:
        print("Wallet amount is insufficient for this order. Please add more money to the wallet.")
        return

    wallet_amount -= total_price
    order_placed_label.config(text=f"Order placed successfully! Order ID: {order_id}")
    wallet_amount_label.config(text=f"Wallet Amount: {wallet_amount} rupees")
    reviewOrders();

def updateOrderStatus():
    order_id = int(input("Enter order ID to update status: "))

    if order_id in orders:
        status = input("Enter new status: ")
        orders[order_id]['status'] = status
        print("Order status updated successfully!")
    else:
        print("Order ID not found.")

    order_status_updated_label.config(text="Order status updated successfully!")    

def reviewOrders():
    orders_table.delete(*orders_table.get_children())
    filter_choice = filter_choice_var.get()
    headers = ["Order ID", "Customer Name", "Order Items", "Status", "Total Price"]
    rows = []
    for order_id, order in orders.items():
        if filter_choice == '1' or (filter_choice == '2' and order['status'] == 'received') or \
           (filter_choice == '3' and order['status'] == 'preparing') or \
           (filter_choice == '4' and order['status'] == 'ready for pickup') or \
           (filter_choice == '5' and order['status'] == 'delivered'):
            order_items = {}
            for dish_id in order['order_items']:
                if dish_id in menu:
                    dish = menu[dish_id]
                    item_name = dish['dish_name']
                    if item_name in order_items:
                        order_items[item_name] += 1
                    else:
                        order_items[item_name] = 1
            order_items_str = ", ".join([f"{quantity}x {item}" for item, quantity in order_items.items()])
            total_price = sum(menu[dish_id]['price'] for dish_id in order['order_items'] if dish_id in menu)
            rows.append([order_id, order['customer_name'], order_items_str, order['status'], total_price])
    
    
    if rows:
        for row in rows:
            orders_table.insert("", tk.END, values=row)
    else:
        messagebox.showinfo("No Orders", "No orders found.")

    global wallet_amount
    total_price = sum(menu[dish_id]['price'] for dish_id in order['order_items'] if dish_id in menu)
    
    if total_price > wallet_amount:
        print("Wallet amount is insufficient for this order. Please add more money to the wallet.")
        return



def addAmountToWallet():
    global wallet_amount
    try:
        amount = float(amount_entry.get())
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        wallet_amount += amount
        print(f"{amount} rupees added to the wallet. Current wallet balance: {wallet_amount} rupees.")
        wallet_amount_label.config(text=f"Wallet Amount: {wallet_amount} rupees")
        amount_entry.delete(0, tk.END)  # Clear the input field
    except ValueError as e:
        print("Invalid amount:", e) 

def showMenu():
    menu_table.delete(*menu_table.get_children())
    for dish_id, dish in menu.items():
        availability = "Yes" if dish['availability'] else "No"
        menu_table.insert("", tk.END, values=[dish_id, dish['dish_name'], dish['price'], dish['stocks'], availability])

def handleChoice(choice):
    if choice == '1':
        showMenu()
    elif choice == '2':
        addDish()
    elif choice == '3':
        removeDish()
    elif choice == '4':
        updateAvailability()
    elif choice == '5':
        takeOrders()
    elif choice == '6':
        updateOrderStatus()
    elif choice == '7':
        reviewOrders()
    elif choice == '8':
        root.quit()
    else:
        messagebox.showinfo("Invalid choice", "Please try again.")

root = tk.Tk()
root.title("Zomato Chronicles: The Great Food Fiasco")

# Create a label
title_label = tk.Label(root, text="Zomato Chronicles: The Great Food Fiasco")
title_label.pack()

# Create buttons for each menu option
button_frame = tk.Frame(root)
button_frame.pack()

button_show_menu = tk.Button(button_frame, text="Show Menu", command=showMenu)
button_show_menu.pack(side=tk.LEFT)

button_add_dish = tk.Button(button_frame, text="Add a New Dish", command=addDish)
button_add_dish.pack(side=tk.LEFT)

button_remove_dish = tk.Button(button_frame, text="Remove a Dish", command=removeDish)
button_remove_dish.pack(side=tk.LEFT)

button_update_availability = tk.Button(button_frame, text="Update Dish Availability", command=updateAvailability)
button_update_availability.pack(side=tk.LEFT)

button_take_order = tk.Button(button_frame, text="Take a New Order", command=takeOrders)
button_take_order.pack(side=tk.LEFT)

button_update_order_status = tk.Button(button_frame, text="Update Order Status", command=updateOrderStatus)
button_update_order_status.pack(side=tk.LEFT)

button_review_orders = tk.Button(button_frame, text="Review All Orders", command=reviewOrders)
button_review_orders.pack(side=tk.LEFT)

button_exit = tk.Button(button_frame, text="Exit", command=root.quit)
button_exit.pack(side=tk.LEFT)

amount_frame = tk.Frame(root)
amount_frame.pack(pady=10)

amount_label = tk.Label(amount_frame, text="Add Amount to Wallet:", font=("Arial", 12))
amount_label.pack(side=tk.LEFT)

amount_entry = tk.Entry(amount_frame, font=("Arial", 12), width=10)
amount_entry.pack(side=tk.LEFT)

button_add_amount = tk.Button(amount_frame, text="Add", font=("Arial", 12), command=addAmountToWallet)
button_add_amount.pack(side=tk.LEFT)

# ... (rest of the code remains the same)

# Create a label for displaying the wallet amount
wallet_amount_label = tk.Label(root, text=f"Wallet Amount: {wallet_amount} rupees", font=("Arial", 12))
wallet_amount_label.pack()

# Create labels for displaying messages
dish_added_label = tk.Label(root, text="")
dish_added_label.pack()

dish_removed_label = tk.Label(root, text="")
dish_removed_label.pack()

availability_updated_label = tk.Label(root, text="")
availability_updated_label.pack()

order_placed_label = tk.Label(root, text="")
order_placed_label.pack()

order_status_updated_label = tk.Label(root, text="")
order_status_updated_label.pack()

# Menu Table
menu_frame = tk.Frame(root)
menu_frame.pack(pady=10)

menu_label = tk.Label(menu_frame, text="Menu", font=("Arial", 14))
menu_label.pack()

menu_table = ttk.Treeview(menu_frame, columns=["Dish ID", "Dish Name", "Price", "Stocks", "Availability"])
menu_table.column("#0", width=0, stretch=tk.NO)  # Hide the empty column
menu_table.column("Dish ID", width=80, anchor=tk.CENTER)
menu_table.heading("Dish ID", text="Dish ID")
menu_table.column("Dish Name", width=200, anchor=tk.CENTER)
menu_table.heading("Dish Name", text="Dish Name")
menu_table.column("Price", width=80, anchor=tk.CENTER)
menu_table.heading("Price", text="Price")
menu_table.column("Stocks", width=80, anchor=tk.CENTER)
menu_table.heading("Stocks", text="Stocks")
menu_table.column("Availability", width=100, anchor=tk.CENTER)
menu_table.heading("Availability", text="Availability")
menu_table.pack()


# Orders Table
orders_frame = tk.Frame(root)
orders_frame.pack(pady=10)

orders_label = tk.Label(orders_frame, text="Orders", font=("Arial", 14))
orders_label.pack()

# Create a frame for filtering orders
filter_frame = tk.Frame(root)
filter_frame.pack()

filter_label = tk.Label(filter_frame, text="Filter Orders:")
filter_label.pack(side=tk.LEFT)

filter_choice_var = tk.StringVar()
filter_choice_var.set('1')

filter_all_orders_radio = tk.Radiobutton(filter_frame, text="All Orders", variable=filter_choice_var, value='1')
filter_all_orders_radio.pack(side=tk.LEFT)

filter_received_orders_radio = tk.Radiobutton(filter_frame, text="Received Orders", variable=filter_choice_var, value='2')
filter_received_orders_radio.pack(side=tk.LEFT)

filter_preparing_orders_radio = tk.Radiobutton(filter_frame, text="Preparing Orders", variable=filter_choice_var, value='3')
filter_preparing_orders_radio.pack(side=tk.LEFT)

filter_ready_orders_radio = tk.Radiobutton(filter_frame, text="Ready for Pickup Orders", variable=filter_choice_var, value='4')
filter_ready_orders_radio.pack(side=tk.LEFT)

filter_delivered_orders_radio = tk.Radiobutton(filter_frame, text="Delivered Orders", variable=filter_choice_var, value='5')
filter_delivered_orders_radio.pack(side=tk.LEFT)

orders_table = ttk.Treeview(orders_frame, columns=["Order ID", "Customer Name", "Order Items", "Status", "Total Price"])
orders_table.column("#0", width=0, stretch=tk.NO)  # Hide the empty column
orders_table.column("Order ID", width=80, anchor=tk.CENTER)
orders_table.heading("Order ID", text="Order ID")
orders_table.column("Customer Name", width=150, anchor=tk.CENTER)
orders_table.heading("Customer Name", text="Customer Name")
orders_table.column("Order Items", width=200, anchor=tk.CENTER)
orders_table.heading("Order Items", text="Order Items")
orders_table.column("Status", width=150, anchor=tk.CENTER)
orders_table.heading("Status", text="Status")
orders_table.column("Total Price", width=100, anchor=tk.CENTER)
orders_table.heading("Total Price", text="Total Price")
orders_table.pack()




# Run the Tkinter event loop
root.mainloop()