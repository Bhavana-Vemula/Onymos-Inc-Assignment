# Onymos-Inc-Assignment

A **real-time stock trading engine** that simulates Buy and Sell orders, efficiently matches them, and handles concurrency using lock-free data structures.  

## **Features**  
- ✅ Supports **1,024 tickers (T0 - T1023)**  
- ✅ Efficient **O(n) order matching**  
- ✅ **Lock-free concurrency** for handling trades in multiple threads  
- ✅ **Randomized simulation** of Buy/Sell orders  
- ✅ Clean, modular structure for **scalability and maintenance**  


## **How It Works**  
1. **Orders are added randomly** (`Buy` or `Sell`).  
2. **Orders are stored** in an array-based order book.  
3. **Matching logic** finds and executes trades based on price.  
4. **Multi-threading** allows simultaneous order placement and matching.  
5. **Simulation runs for 5 seconds** before stopping automatically.  

## **Installation & Running**  
### **1. Clone the repository**  
```sh
git clone https://github.com/yourusername/your-repo.git
```
```sh
cd your-repo
```
2. Run the simulation
```py
python main.py
```
Example Output

Added order: Order(Buy, T45, Q:10, P:500.0)
Added order: Order(Sell, T45, Q:5, P:495.0)
Matching: Order(Buy, T45, Q:10, P:500.0) with Order(Sell, T45, Q:5, P:495.0) for Q:5
Contributing

Feel free to fork this repository and improve the project!

📧 Contact: [Your Name] - [Your Email]
