from abc import ABC, abstractmethod


class PaymentGateway(ABC):

    @abstractmethod
    def pay(self, amount: float):
        pass


class VNPay(PaymentGateway):

    def pay(self, amount: float):
        return f"Thanh toán {amount:,.0f} VNĐ qua VNPay"


class Momo(PaymentGateway):

    def pay(self, amount: float):
        return f"Thanh toán {amount:,.0f} VNĐ qua Momo"


class CreditCard(PaymentGateway):

    def pay(self, amount: float):
        return f"Thanh toán {amount:,.0f} VNĐ qua Credit Card"