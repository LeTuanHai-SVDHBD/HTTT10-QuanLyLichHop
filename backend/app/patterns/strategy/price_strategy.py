from abc import ABC, abstractmethod


class PriceStrategy(ABC):

    @abstractmethod
    def calculate_price(self, price: float) -> float:
        pass

class NormalPriceStrategy(PriceStrategy):

    def calculate_price(self, price: float) -> float:
        return price

class FlashSaleStrategy(PriceStrategy):

    def calculate_price(self, price: float) -> float:
        discount = 0.20
        return price * (1 - discount)