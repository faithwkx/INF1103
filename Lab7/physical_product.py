
from product import Product


# PhysicalProduct inherits from Product
class PhysicalProduct(Product):

    # Initialise product details and weight
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    # Display product information and additional weight
    def display_information(self):
        super().display_information()
        print("Weight:", self.__weight, "kg")

    # Provide fulfilment information for physical products
    def get_fulfilment_info(self):
        return "This product requires physical shipping."
