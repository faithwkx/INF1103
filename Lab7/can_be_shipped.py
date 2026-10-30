
from abc import ABC, abstractmethod


# Interface for objects that can be shipped
class CanBeShipped(ABC):

    # Require implementing classes to calculate shipping costs
    @abstractmethod
    def calculate_shipping_cost(self):
        pass
