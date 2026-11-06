

from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


# Create a Supplier independently.
supplier = Supplier("S001", "Apple", "apple@example.com")

# Create two different Products using the same Supplier object.
laptop = PhysicalProduct("P001", "MacBook", 1500.0, 10, 2.0, supplier)
software = DigitalProduct("D001", "Software", 100.0, 50, 500.0, supplier)

# Display product and supplier information.
print("=== Physical Product ===")
laptop.display_information()

print("\n=== Digital Product ===")
software.display_information()

# PREDICT FIRST:
# What happens if we delete the supplier variable?
# Will both products still access their Supplier?

del supplier

print("\n=== After deleting supplier variable ===")
print("Laptop Supplier:", laptop.supplier.name)
print("Software Supplier:", software.supplier.name)

# Confirm both products share the same Supplier object.
print("Same Supplier Object:", laptop.supplier is software.supplier)
