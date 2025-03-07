import threading
import random
import time
from order_book import add_order
from order_matcher import match_order

running = True

def simulate_add_orders():
    """
    Simulates random stock transactions.
    """
    while running:
        order_type = random.choice(["Buy", "Sell"])
        ticker = "T" + str(random.randint(0, 1023))
        quantity = random.randint(1, 100)
        price = round(random.uniform(10, 1000), 2)
        
        add_order(order_type, ticker, quantity, price)
        time.sleep(0.01)  # Simulate delay

def simulate_match_orders():
    """
    Continuously attempts to match orders for random tickers.
    """
    while running:
        ticker = "T" + str(random.randint(0, 1023))
        match_order(ticker)
        time.sleep(0.01)


def stop_simulation():
    """
    Stops the simulation after a fixed duration.
    """
    global running
    time.sleep(5)  # Run for 5 seconds
    running = False  # Stop threads

if __name__ == "__main__":
    # Start simulation threads
    threads = []
    
    t1 = threading.Thread(target=simulate_add_orders)
    t2 = threading.Thread(target=simulate_match_orders)
    
    threads.append(t1)
    threads.append(t2)

    # Start threads
    t1.start()
    t2.start()

    # Stop simulation after 5 seconds
    stop_simulation()

    # Wait for threads to finish
    for t in threads:
        t.join()

    print("Simulation complete.")
