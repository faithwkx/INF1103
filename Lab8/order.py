
from product import Product
from order_line import OrderLine


class Order:

    # Initialise the order with a unique ID and empty order lines.
    def __init__(self, order_id: str) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    # Composition: Order creates its own OrderLine objects.
    def add_order_line(self, product: Product, quantity: int) -> None:

        # Validate that the ordered quantity is positive.
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        # Create the OrderLine inside the Order, not externally.
        order_line = OrderLine(product, quantity)

        # Store the OrderLine in this Order.
        self.order_lines.append(order_line)

        print("Order line added successfully.")

    # Remove an OrderLine through its owning Order.
    def remove_order_line(self, product_id: str) -> None:
        for order_line in self.order_lines:
            if order_line.product.get_product_id() == product_id:
                self.order_lines.remove(order_line)
                print("Order line removed successfully.")
                return

        print("Order line not found.")

    # Calculate the total cost by adding all order line subtotals.
    def calculate_total(self) -> float:
        total: float = 0.0

        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()

        return total

    # Display all OrderLines and the overall order total.
    def display_order(self) -> None:
        print("Order ID:", self.order_id)

        if not self.order_lines:
            print("No items in this order.")
            return

        for order_line in self.order_lines:
            print("------------------------------")
            order_line.display_information()

        print("------------------------------")
        print(f"Order Total: ${self.calculate_total():.2f}")
