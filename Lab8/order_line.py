
# INF1103 Lab 8 - OrderLine Class
# Section 4.1: Composition between Order and OrderLine
#
# An OrderLine represents one Product and its ordered quantity.
# The Order creates and manages its OrderLine objects.
# OrderLine refers to a Product but does not own the Product.

from product import Product


class OrderLine:

    # Initialise the product and quantity for this order line.
    def __init__(self, product: Product, quantity: int) -> None:

        # Association: Refer to an existing Product object.
        self.product: Product = product
        self.quantity: int = quantity

    # Calculate the cost of this order line.
    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity

    # Display the order line's product, quantity and subtotal.
    def display_information(self) -> None:
        print("Product ID:", self.product.get_product_id())
        print("Quantity:", self.quantity)
        print(f"Subtotal: ${self.calculate_subtotal():.2f}")
