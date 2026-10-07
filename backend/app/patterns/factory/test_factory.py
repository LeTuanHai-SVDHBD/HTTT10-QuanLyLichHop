from app.patterns.factory.payment_factory import PaymentFactory

payment1 = PaymentFactory.create_payment("vnpay")
payment2 = PaymentFactory.create_payment("momo")
payment3 = PaymentFactory.create_payment("credit_card")

print(payment1.pay(500000))
print(payment2.pay(500000))
print(payment3.pay(500000))

