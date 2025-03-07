from order_book import order_books, get_ticker_index

def match_order(ticker):
    """
    Matches Buy and Sell orders for the given ticker.
    """
    index = get_ticker_index(ticker)
    book = order_books[index]

    while True:
        # Find the lowest-priced Sell order
        lowest_sell = None
        lowest_sell_index = -1
        for i, sell in enumerate(book.sell_orders):
            if sell is not None and (lowest_sell is None or sell.price < lowest_sell.price):
                lowest_sell = sell
                lowest_sell_index = i

        if lowest_sell is None:
            break  # No sell orders available

        # Find a Buy order that matches the lowest Sell order
        matched = False
        for j, buy in enumerate(book.buy_orders):
            if buy is not None and buy.price >= lowest_sell.price:
                traded_quantity = min(buy.quantity, lowest_sell.quantity)
                print(f"Matching: {buy} with {lowest_sell} for Q:{traded_quantity}")

                buy.quantity -= traded_quantity
                lowest_sell.quantity -= traded_quantity

                if buy.quantity == 0:
                    book.buy_orders[j] = None
                if lowest_sell.quantity == 0:
                    book.sell_orders[lowest_sell_index] = None
                
                matched = True
                break  # Break after first match

        if not matched:
            break  # No matching buy order found

        # Clean up completed orders
        book.buy_orders = [o for o in book.buy_orders if o is not None]
        book.sell_orders = [o for o in book.sell_orders if o is not None]
