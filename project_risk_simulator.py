import math
import random
import sys
import yfinance as yf
import matplotlib.pyplot as plt

def main():
    # 1. Collect user inputs for the simulation
    try:
        ticker_symbol = input("Ticker symbol (e.g., AAPL, MSFT): ").strip().upper()
        days = int(input("Time horizon in days (e.g., 365): ").strip())
        if days <= 0:
            raise ValueError("Number of days must be a positive integer.")
    except ValueError as ve:
        sys.exit(f"Input Error: {ve}")
    
    # 2. Fetch the latest market price and run simulation
    start_price = get_live_price(ticker_symbol)
    drift, volatility = get_historical_parameters(ticker_symbol)
    
    prices = simulate_prices(start_price, days, volatility, drift)
    
    # 3. Calculate statistical risk metrics
    max_p, min_p, avg_p, var_95 = calculate_metrics(prices)
    
    # 4. Display the results in the terminal
    print("-" * 30)
    print(f"Simulation for {days} days completed.")
    print(f"Ticker: {ticker_symbol.upper()}")
    print(f"Starting Price: {start_price:.2f}€")
    print(f"Highest price: {max_p:.2f}€")
    print(f"Lowest price: {min_p:.2f}€")
    print(f"Average: {avg_p:.2f}€")
    print(f"VaR (95% Confidence Level): {var_95:.2f}€")
    print(f"Final price: {prices[-1]:.2f}€")
    plot_prices(prices)

def get_live_price(ticker_symbol):
    """Fetches the latest closing price using yfinance."""
    try:
        ticker = yf.Ticker(ticker_symbol)
        # Fetch 5 days to ensure we get data even on weekends
        data = ticker.history(period="5d")
        
        if data.empty:
            sys.exit(f"Error: No data found for ticker '{ticker_symbol}'.")
            
        # Use .iloc[-1] to get the most recent closing price
        return data['Close'].iloc[-1]
    except Exception as e:
        sys.exit(f"Error fetching live price: {e}")
    
def get_historical_parameters(ticker_symbol):
    """Calculates drift and volatility from the last year of market data."""
    try:
        ticker = yf.Ticker(ticker_symbol)
        # Fetch 1 year of historical data
        data = ticker.history(period="1y")
        
        if len(data) < 20:
            sys.exit("Error: Not enough historical data to calculate drift.")

        # Calculate daily percentage changes
        # (Price_today / Price_yesterday) - 1
        returns = data['Close'].pct_change().dropna()

        # Calculate average daily return and annualize it (252 trading days)
        avg_daily_return = returns.mean()
        drift = avg_daily_return * 252
        
        # Bonus: We can also calculate volatility automatically!
        volatility = returns.std() * math.sqrt(252)

        return drift, volatility
    except Exception as e:
        sys.exit(f"Error calculating historical parameters: {e}")


def simulate_prices(start_price, days, volatility, drift):
    """Simulates a price path using Geometric Brownian Motion (GBM)."""
    prices = [start_price]
    # Time step (daily, assuming 365 days per year)
    dt = 1/365
    
    for _ in range(days):
        epsilon = random.gauss(0, 1)
        # GBM formula: S_t = S_0 * exp((mu - 0.5 * sigma^2) * dt + sigma * epsilon * sqrt(dt))
        change = math.exp((drift - 0.5 * volatility**2) * dt + 
                          volatility * epsilon * math.sqrt(dt))
        prices.append(prices[-1] * change)
    return prices

def calculate_metrics(price_paths):
    """Calculates key risk indicators from the simulated data."""
    max_price = max(price_paths)
    min_price = min(price_paths)
    avg_price = sum(price_paths) / len(price_paths)
    
    # Value at Risk (VaR) at 95% confidence:
    # We sort the simulated prices and find the 5th percentile
    sorted_prices = sorted(price_paths)
    index_95 = int(0.05 * len(sorted_prices))
    var_95 = sorted_prices[index_95]

    return max_price, min_price, avg_price, var_95

def plot_prices(prices):
    """Optional: Plots the simulated price path."""
    try:
        import matplotlib.pyplot as plt
        plt.plot(prices)
        plt.title("Simulated Price Path")
        plt.xlabel("Days")
        plt.ylabel("Price (€)")
        plt.grid(True)
        plt.show()
    except ImportError:
        print("matplotlib is not installed. Skipping plot.")

if __name__ == "__main__":
    main()