
# INF1103 Lab 8 - Supplier Class
# Section 2.1: Association between Supplier and Product
#
# A Supplier can supply many Products.
# Supplier and Product can exist independently of each other.


class Supplier:
    # Constructor: Sets up the supplier's information
    def __init__(self, supplier_id: str, name: str, contact_email: str):
        self.supplier_id: str = supplier_id
        self.name: str = name
        self.contact_email: str = contact_email

    # Displays the supplier's information
    def display_information(self) -> None:
        print("Supplier ID:", self.supplier_id)
        print("Supplier Name:", self.name)
        print("Contact Email:", self.contact_email)


# Test the Supplier class
if __name__ == "__main__":
    supplier = Supplier("S001", "Apple", "apple@example.com")
    supplier.display_information()
