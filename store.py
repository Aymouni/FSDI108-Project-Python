from catalog import catalog # Import your catalog list.

# Global shopping cart
cart = []

# Helper functions (store name/menu)
def print_header(text):
    print("----------------------")
    print(text)
    print("----------------------")

def print_menu():
    print("Menu")
    print("1.- View Catalog")
    print("2.- Search Product")
    print("3.- View Cart")
    print("4.- Clear Cart")
    # Add more option if needed
    print("Q.- Quit")

# Catalog and Cart functions

def print_catalog():
    print_header("- Our Catalog -")
    for prod in catalog:    # ljust means justiy left 15 spaces to the right
        print(f"| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}")

    answer = input("Type ID to add (N to close): ")
    if answer.lower() == "n":
        return
    else:
        add_product_to_cart(answer)
    print("----------------------")

def add_product_to_cart(prod_id):
    found = False
    for prod in catalog:
        if str(prod["id"]) == str(prod_id):
            found = True
            cart.append(prod)   # Add product to the cart
            print(f"{prod["title"]} added to your cart")
            break

    if not found:
        print("Item does not exist")

def search_product():
    text = input("Search text: ").lower()
    found = False
    for prod in catalog:
        if text in prod["title"].lower():
            found = True
            print(f"| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}")
            choice = input("Do you want to add this item to the cart? (y/n): ")
            if choice.lower() == "y":
                add_product_to_cart(prod["id"])
            break # Stops after first match
    
    if not found:
        print("Sorry, this item doesn't exist.")
    print("----------------------")

def view_cart():
    print_header("Your Cart")
    if not cart:
        print("Your cart is empty.")
    else:
        for prod in cart:
            print(f"| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}")
        cart_total()    # Shows total price

def cart_total():
    total = 0 # Start from 0 and add the prices up
    for prod in cart:
        total += prod["price"] # Add product proce to total
    print(f"Total is: ${total}")

def clear_cart():
    cart.clear()    # Clearing the cart
    print("Your cart has been cleared")

# Main program loop
option = ""
while option != "q" and option != "Q":
    print_header("Welcome to Our Store")
    print_menu()

    option = input("Choose an option: ")

    if option == "1":
        print_catalog()
    elif option == "2":
        search_product()
    elif option == "3":
        view_cart()
    elif option == "4":
        clear_cart()
    elif option == "q" or option == "Q":
        print("Good Bye!")
        break
    else:
        print("** Error: invalid option")
        print("----------------------")

    