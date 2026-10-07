from .payment_gateway import VNPay, Momo, CreditCard


class PaymentFactory:

    @staticmethod
    def create_payment(method: str):

        if method == "vnpay":
            return VNPay()

        if method == "momo":
            return Momo()

        if method == "credit_card":
            return CreditCard()

        raise ValueError("Phương thức thanh toán không hợp lệ")