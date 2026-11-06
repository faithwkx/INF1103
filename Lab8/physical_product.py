
from product import Product
from supplier import Supplier
from can_be_shipped import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):

    # Initialise product details, weight and Supplier.
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        weight: float,
        supplier: Supplier
    ) -> None:

        # Pass common product details to the parent Product class.
        super().__init__(product_id, name, price, stock, supplier)

        # Weight belongs specifically to a physical product.
        self.__weight: float = weight

    # Method overriding: Display common details and physical weight.
    def display_information(self) -> None:
        super().display_information()
        print("Weight:", self.__weight, "kg")

    # Polymorphism: Physical products require shipping.
    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    # Implement the CanBeShipped interface.
    def calculate_shipping_cost(self) -> float:
        return self.__weight * 2

    # Convert physical product information into a dictionary for JSON.
    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data
