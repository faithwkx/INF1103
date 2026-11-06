
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order


# Create an independent Supplier.
supplier = Supplier("S001", "Apple", "apple@example.com")

# Create two independent Products.
laptop = PhysicalProduct(
    "P001", "MacBook", 1500.0, 10, 2.0, supplier
)

software = DigitalProduct(
    "D001", "Software", 100.0, 50, 500.0, supplier
)

# Create the first Order.
order1 = Order("O001")

# Order creates two OrderLine objects.
order1.add_order_line(laptop, 2)
order1.add_order_line(software, 3)

print("\n=== Order 1 ===")
order1.display_order()

# Create a second Order using the same laptop Product.
order2 = Order("O002")
order2.add_order_line(laptop, 1)

print("\n=== Order 2 ===")
order2.display_order()

# Verify separate OrderLines refer to the same Product object.
print("\n=== Checking Object Identity ===")

print(
    "Same Product:",
    order1.order_lines[0].product is order2.order_lines[0].product
)

print(
    "Same OrderLine:",
    order1.order_lines[0] is order2.order_lines[0]
)

# Remove the laptop OrderLine from Order 1.
print("\n=== Removing OrderLine from Order 1 ===")
order1.remove_order_line("P001")

print("\n=== Order 1 After Removal ===")
order1.display_order()

# The Product and Order 2 are unaffected.
print("\n=== Laptop Still Exists ===")
laptop.display_information()

print("\n=== Order 2 Still Exists ===")
order2.display_order()
