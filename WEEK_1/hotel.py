menu = []
orders = []

def add_menu_item():
    name = input("Item name: ")
    price = float(input("Price: "))
    menu.append([name, price])
    print("Item added.\n")

def take_order():
    print("Menu:")
    for i, item in enumerate(menu):
        print(i + 1, item[0], "$", item[1])
    choice = int(input("Choose item number: "))
    qty = int(input("Quantity: "))
    if 1 &lt;= choice &lt;= len(menu):
        item = menu[choice - 1]
        orders.append([item[0], item[1], qty])
        print("Order added.\n")
    else:
        print("Invalid choice.\n")

def show_bill():
    total = 0
    print("\nBill:")
    for order in orders:
        name, price, qty = order
        cost = price * qty
        print(name, qty, "x", price, "=", cost)
        total += cost
    print("Total: $", total, "\n")

def main():
    while True:
        print("1.Add Menu Item 2.Take Order 3.Show Bill 4.Exit")
        choice = input("Choice: ")
        if choice == '1':
            add_menu_item()
        elif choice == '2':
            take_order()
        elif choice == '3':
            show_bill()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Try again.\n")

if __name__ == "__main__":
    main()
