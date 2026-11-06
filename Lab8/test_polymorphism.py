
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


# Step 1: Create an independent Supplier object.
supplier = Supplier("S001", "Apple", "apple@example.com")


# Step 2: Create two different types of Products.
laptop = PhysicalProduct(
    "P001", "MacBook", 1500.0, 10, 2.0, supplier
)

software = DigitalProduct(
    "D001", "Software", 100.0, 50, 500.0, supplier
)


# Step 3: Create one Inventory that stores both types.
inventory = Inventory()

inventory.add_product(laptop)
inventory.add_product(software)


# Step 4: Demonstrate polymorphism using one loop.
print("\n=== Polymorphism Test ===")

for product in inventory.products:

    # Python selects the correct subclass implementation.
    product.display_information()

    # Same method name, different subclass behaviour.
    print("Fulfilment:", product.get_fulfilment_info())

    print("------------------------------")


# Step 5: Verify both objects work through Product references.
print("\n=== Test Completed ===")
print("Total Products:", len(inventory.products))
