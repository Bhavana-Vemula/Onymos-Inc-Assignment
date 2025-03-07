from order import Order

class OrderBook:
    def __init__(self):
        self.buy_orders = []   # List to store buy orders
        self.sell_orders = []  # List to store sell orders

# Create an array of 1024 order books, each indexed by ticker (T0 - T1023)
order_books = [OrderBook() for _ in range(1024)]

def get_ticker_index(ticker):
    """
    Converts a ticker symbol like 'T123' into an index for order_books.
    """
    return int(ticker[1:])

def add_order(order_type, ticker, quantity, price):
    """
    Adds a new order to the order book.
    """
    index = get_ticker_index(ticker)
    order = Order(order_type, ticker, quantity, price)
    
    if order_type == "Buy":
        order_books[index].buy_orders.append(order)
    elif order_type == "Sell":
        order_books[index].sell_orders.append(order)
    
    print("Added order:", order)
