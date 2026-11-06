
from product import Product


class Inventory:

    # Initialise an empty collection of Product objects.
    def __init__(self) -> None:
        self.products: list[Product] = []

    # Add an existing Product object to Inventory.
    def add_product(self, product: Product) -> None:
        self.products.append(product)
        print("Product added successfully.")

    # Remove a Product reference using its product ID.
    def remove_product(self, product_id: str) -> None:
        for product in self.products:
            if product.get_product_id() == product_id:
                self.products.remove(product)
                print("Product removed successfully.")
                return

        print("Product not found.")

    # Find and return a Product, or None if it does not exist.
    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.get_product_id() == product_id:
                return product

        return None

    # Display all Products using polymorphism.
    def display_all_products(self) -> None:
        if not self.products:
            print("Inventory is empty.")
            return

        for product in self.products:
            product.display_information()
            print("Fulfilment:", product.get_fulfilment_info())
            print("------------------------------")
