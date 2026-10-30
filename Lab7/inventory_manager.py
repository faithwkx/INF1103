
import json
import os
from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

# Create an inventory object
inventory = Inventory()


# Display the main menu
def display_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


# Add a new physical or digital product
def add_product():
    print("\nAdd New Product")
    print("1. Physical Product")
    print("2. Digital Product")

    product_type = input("Choose product type: ")

    if product_type not in ("1", "2"):
        print("Invalid product type.")
        return

    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    if product_type == "1":
        weight = float(input("Weight (kg): "))
        product = PhysicalProduct(
            product_id, name, price, stock, weight
        )

    else:
        download_size = float(input("Download Size (MB): "))
        product = DigitalProduct(
            product_id, name, price, stock, download_size
        )

    inventory.add_product(product)


# Update stock quantity
def update_stock():
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)

    if product is not None:
        print("\nProduct Found:")
        product.display_information()

        new_stock = int(input("\nNew Stock Quantity: "))
        product.update_stock(new_stock)

        print("\nStock updated successfully!")
    else:
        print("Product not found.")


# Search for a product
def search_product():
    print("\nSearch Product")

    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)

    if product is not None:
        print("\nProduct Found")
        print("----------------------------------------")
        product.display_information()
        print("----------------------------------------")
    else:
        print("Product not found.")


# Load inventory from JSON
def load_inventory():
    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            if item["type"] == "physical":
                product = PhysicalProduct(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["weight"]
                )

            elif item["type"] == "digital":
                product = DigitalProduct(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["download_size"]
                )

            else:
                raise ValueError("Unknown product type.")

            inventory.add_product(product)

        print("Inventory loaded successfully.")
    else:
        print("inventory.json not found.")
        print("Starting with empty inventory.")


# Save inventory to JSON
def save_inventory():
    data = []

    for product in inventory.products:
        data.append(product.to_dict())

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully.")


# Main program
print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================")

load_inventory()

while True:
    display_menu()

    option = input("Enter option: ")

    if option == "1":
        inventory.display_all()

    elif option == "2":
        add_product()

    elif option == "3":
        update_stock()

    elif option == "4":
        search_product()

    elif option == "5":
        print("\nSaving inventory...")
        save_inventory()

    elif option == "6":
        print("\nSaving inventory before exit...")
        save_inventory()

        print("\nThank you for using Inventory Management System.")
        print("Program terminated.")
        break

    else:
        print("Invalid option. Please enter 1 to 6.")
