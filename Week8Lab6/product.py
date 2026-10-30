
class Product:
    # Initialise product details
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    # Get the product ID
    def get_product_id(self):
        return self.__product_id

    # Update stock quantity
    def update_stock(self, quantity):
        self.__stock = quantity

    # Display product information
    def display_information(self):
        print("ID:", self.__product_id)
        print("Name:", self.__name)
        print("Price: $", format(self.__price, ".2f"), sep="")
        print("Stock:", self.__stock)
