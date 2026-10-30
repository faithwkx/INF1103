
class Inventory:
    # Initialise an empty inventory
    def __init__(self):
        self.products = []

    # Add a product to the inventory
    def add_product(self, product):
        self.products.append(product)
        print("Product added successfully!")

    # Search for a product by its ID
    def search_product(self, product_id):
        for product in self.products:
            if product.get_product_id() == product_id:
                return product

        return None

    # Display all products in the inventory
    def display_all(self):
        print("\nCurrent Inventory")
        print("----------------------------------------")

        for product in self.products:
            product.display_information()
            print("----------------------------------------")
