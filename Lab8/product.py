
from abc import ABC, abstractmethod
from supplier import Supplier


# Abstract Product class
class Product(ABC):

    # Initialise product details and associate a Supplier object
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        supplier: Supplier
    ) -> None:
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock

        # Association: Store a reference to an existing Supplier
        self.supplier: Supplier = supplier

    # Get the product ID
    def get_product_id(self) -> str:
        return self.__product_id

    # Get the product price for OrderLine calculations
    @property
    def price(self) -> float:
        return self.__price

    # Update stock quantity
    def update_stock(self, quantity: int) -> None:
        self.__stock = quantity

    # Display product and supplier information
    def display_information(self) -> None:
        print("ID:", self.__product_id)
        print("Name:", self.__name)
        print("Price: $", format(self.__price, ".2f"), sep="")
        print("Stock:", self.__stock)
        print("Supplier:", self.supplier.name)
        print("Supplier Email:", self.supplier.contact_email)

    # Convert product details into a dictionary for JSON saving
    def to_dict(self) -> dict:
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier_id": self.supplier.supplier_id,
            "supplier_name": self.supplier.name,
            "supplier_email": self.supplier.contact_email
        }

    # Require subclasses to provide fulfilment information
    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass
