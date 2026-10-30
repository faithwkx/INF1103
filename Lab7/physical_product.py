
from product import Product
from can_be_shipped import CanBeShipped


# PhysicalProduct inherits from Product and implements CanBeShipped
class PhysicalProduct(Product, CanBeShipped):

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

    # Calculate shipping cost based on product weight
    def calculate_shipping_cost(self):
        return self.__weight * 2

    
    # Convert physical product details into a dictionary
    def to_dict(self):
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data

