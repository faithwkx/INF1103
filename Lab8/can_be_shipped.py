
from abc import ABC, abstractmethod


class CanBeShipped(ABC):

    # Subclasses must implement their own shipping cost calculation.
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass
