from app.patterns.strategy.price_strategy import (
    NormalPriceStrategy,
    FlashSaleStrategy
)


price = 500000

normal = NormalPriceStrategy()
flash_sale = FlashSaleStrategy()

print("Giá thông thường:", normal.calculate_price(price))
print("Giá Flash Sale:", flash_sale.calculate_price(price))