
from product import Product
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


# This function accepts any Product subclass.
# It does not need to know the specific product type.
def show_product_details(product: Product) -> None:
    product.display_information()
    print("Fulfilment:", product.get_fulfilment_info())


# Create Supplier independently of the Products.
supplier = Supplier("S001", "Apple", "apple@example.com")

# Create PhysicalProduct and DigitalProduct objects.
laptop = PhysicalProduct(
    "P001", "MacBook", 1500.0, 10, 2.0, supplier
)

software = DigitalProduct(
    "D001", "Software", 100.0, 50, 500.0, supplier
)


# Test 1: Both subclasses can replace the parent Product.
print("=== Physical Product LSP Test ===")
show_product_details(laptop)

print("\n=== Digital Product LSP Test ===")
show_product_details(software)


# Test 2: Inventory works with both Product subclasses.
print("\n=== Inventory LSP Test ===")

inventory = Inventory()
inventory.add_product(laptop)
inventory.add_product(software)

inventory.display_all_products()


# Test 3: Both subclasses support Product's stock update method.
print("\n=== Stock Update LSP Test ===")

laptop.update_stock(15)
software.update_stock(100)

print("Stock updated successfully for both product types.")

# Demonstrates that common parent behaviour works
# without requiring special subclass checks.


# Test 4: Confirm both objects are valid Product instances.
print("\n=== Product Substitution Check ===")

print("Laptop is Product:", isinstance(laptop, Product))
print("Software is Product:", isinstance(software, Product))
