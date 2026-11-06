
from supplier import Supplier
from physical_product import PhysicalProduct
from inventory import Inventory


# Create Supplier and Product independently of Inventory.
supplier = Supplier("S001", "Apple", "apple@example.com")

laptop = PhysicalProduct(
    "P001", "MacBook", 1500.0, 10, 2.0, supplier
)

# Create two separate inventories.
inventory_a = Inventory()
inventory_b = Inventory()

# Add laptop to Inventory A.
print("=== Adding Product to Inventory A ===")
inventory_a.add_product(laptop)
inventory_a.display_all_products()

# Remove the laptop from Inventory A.
print("\n=== Removing Product from Inventory A ===")
inventory_a.remove_product("P001")

# Confirm the Product still exists independently.
print("\n=== Product After Removal ===")
laptop.display_information()

# Transfer the same Product object to Inventory B.
print("\n=== Adding Product to Inventory B ===")
inventory_b.add_product(laptop)
inventory_b.display_all_products()

# Verify that Inventory B references the original laptop.
print("\n=== Checking Object Identity ===")
print("Same Product Object:", inventory_b.find_product("P001") is laptop)

# Confirm Inventory A no longer contains the Product.
print("Inventory A Product:", inventory_a.find_product("P001"))
