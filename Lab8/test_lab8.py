
from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order


# Create independent Supplier and Product objects.
supplier = Supplier("S001", "Apple", "apple@example.com")

laptop = PhysicalProduct(
    "P001", "MacBook", 1500.0, 10, 2.0, supplier
)

software = DigitalProduct(
    "D001", "Software", 100.0, 50, 500.0, supplier
)


# TEST 1: Association
# Products retain their Supplier reference after
# the original supplier variable is deleted.
print("TEST 1: Association")

assert laptop.supplier is software.supplier

del supplier

assert laptop.supplier.name == "Apple"
assert software.supplier.name == "Apple"

print("PASS: Association")


# TEST 2: Aggregation
# Inventory can remove a Product without destroying it.
print("\nTEST 2: Aggregation")

inventory_a = Inventory()
inventory_b = Inventory()

inventory_a.add_product(laptop)
inventory_a.remove_product("P001")

assert inventory_a.find_product("P001") is None

inventory_b.add_product(laptop)

assert inventory_b.find_product("P001") is laptop

print("PASS: Aggregation")


# TEST 3: Composition
# Each Order creates its own OrderLine objects.
print("\nTEST 3: Composition")

order1 = Order("O001")
order2 = Order("O002")

order1.add_order_line(laptop, 2)
order1.add_order_line(software, 3)
order2.add_order_line(laptop, 1)

assert order1.calculate_total() == 3300.0
assert order2.calculate_total() == 1500.0

# Different OrderLines refer to the same Product.
assert order1.order_lines[0] is not order2.order_lines[0]
assert order1.order_lines[0].product is laptop
assert order2.order_lines[0].product is laptop

# Removing an OrderLine does not destroy the Product.
order1.remove_order_line("P001")

assert order1.calculate_total() == 300.0
assert order2.calculate_total() == 1500.0

print("PASS: Composition")


# TEST 4: Liskov Substitution Principle
# Both subclasses work wherever Product is expected.
print("\nTEST 4: LSP")


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


show_product_details(laptop)
show_product_details(software)

# Both subclasses support the parent stock behaviour.
laptop.update_stock(15)
software.update_stock(100)

print("PASS: LSP")


# TEST 5: Polymorphism
# The same Product interface produces specialised behaviour.
print("\nTEST 5: Polymorphism")

inventory_b.add_product(software)

assert len(inventory_b.products) == 2

fulfilment_messages = [
    product.get_fulfilment_info()
    for product in inventory_b.products
]

assert fulfilment_messages == [
    "This product requires physical shipping.",
    "This product is delivered digitally."
]

print("PASS: Polymorphism")


print("\n================================")
print("ALL LAB 8 TESTS PASSED")
print("================================")
