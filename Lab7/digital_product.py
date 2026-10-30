
from product import Product


# DigitalProduct inherits from Product
class DigitalProduct(Product):

    # Initialise product details and download size
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    # Display product information and additional download size
    def display_information(self):
        super().display_information()
        print("Download Size:", self.__download_size, "MB")

    # Provide fulfilment information for digital products
    def get_fulfilment_info(self):
        return "This product is delivered digitally."
