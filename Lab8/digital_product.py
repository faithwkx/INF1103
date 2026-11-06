
from product import Product
from supplier import Supplier


class DigitalProduct(Product):

    # Initialise product details, download size and Supplier.
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        download_size: float,
        supplier: Supplier
    ) -> None:

        # Pass common product details to the parent Product class.
        super().__init__(product_id, name, price, stock, supplier)

        # Download size belongs specifically to a digital product.
        self.__download_size: float = download_size

    # Method overriding: Display common details and download size.
    def display_information(self) -> None:
        super().display_information()
        print("Download Size:", self.__download_size, "MB")

    # Polymorphism: Digital products are delivered electronically.
    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally."

    # Convert digital product information into a dictionary for JSON.
    def to_dict(self) -> dict[str, str | int | float]:
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data
