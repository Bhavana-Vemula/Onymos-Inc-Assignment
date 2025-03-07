class Order:
    def __init__(self, order_type, ticker, quantity, price):
        self.order_type = order_type  # "Buy" or "Sell"
        self.ticker = ticker          # e.g. "T123"
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Order({self.order_type}, {self.ticker}, Q:{self.quantity}, P:{self.price})"
