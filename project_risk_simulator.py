import math
import random
import sys
import yfinance as yf
import matplotlib.pyplot as plt

def main():
    try:
        ticker_symbol = input("Ticker symbol (e.g., AAPL, MSFT): ").strip().upper()
        days = int(input("Time horizon in days (e.g., 365): ").strip())
        simulations = int(input("Number of simulations (e.g., 1000): ").strip())

        if days <= 0 or simulations <= 0:
            raise ValueError("Days and simulations must be positive integers.")
    except ValueError as ve:
        sys.exit(f"Input Error: {ve}")

    start_price = get_live_price(ticker_symbol)
    drift, volatility = get_historical_parameters(ticker_symbol)

    price_paths = monte_carlo_simulation(
        start_price, days, simulations, volatility, drift
    )

    metrics = calculate_metrics(price_paths)

    print("-" * 30)
    print(f"Monte Carlo Simulation Completed")
    print(f"Ticker: {ticker_symbol}")
    print(f"Simulations: {simulations}")
    print(f"Time Horizon: {days} days")
    print(f"Starting Price: {start_price:.2f}€")
    print(f"Average Final Price: {metrics['average']:.2f}€")
    print(f"Min Final Price: {metrics['min']:.2f}€")
    print(f"Max Final Price: {metrics['max']:.2f}€")
    print(f"VaR (95% Confidence): {metrics['var_95']:.2f}€")

    plot_prices(price_paths)


def get_live_price(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    data = ticker.history(period="5d")

    if data.empty:
        sys.exit(f"No data found for ticker '{ticker_symbol}'.")

    return data["Close"].iloc[-1]


def get_historical_parameters(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    data = ticker.history(period="1y")

    if len(data) < 20:
        sys.exit("Not enough historical data.")

    returns = data["Close"].pct_change().dropna()

    drift = returns.mean() * 252
    volatility = returns.std() * math.sqrt(252)

    return drift, volatility


def simulate_single_path(start_price, days, volatility, drift):
    prices = [start_price]
    dt = 1 / 365

    for _ in range(days):
        z = random.gauss(0, 1)
        change = math.exp(
            (drift - 0.5 * volatility ** 2) * dt
            + volatility * math.sqrt(dt) * z
        )
        prices.append(prices[-1] * change)

    return prices


def monte_carlo_simulation(start_price, days, simulations, volatility, drift):
    return [
        simulate_single_path(start_price, days, volatility, drift)
        for _ in range(simulations)
    ]


def calculate_metrics(price_paths):
    final_prices = [path[-1] for path in price_paths]
    sorted_prices = sorted(final_prices)

    index_95 = int(0.05 * len(sorted_prices))

    return {
        "min": min(final_prices),
        "max": max(final_prices),
        "average": sum(final_prices) / len(final_prices),
        "var_95": sorted_prices[index_95],
    }

def compute_average_path(price_paths):
    num_days = len(price_paths[0])
    average_path = []

    for day in range(num_days):
        day_sum = sum(path[day] for path in price_paths)
        average_path.append(day_sum / len(price_paths))

    return average_path

def plot_prices(price_paths):
    for path in price_paths[:50]:  # limit plotting for readability
        plt.plot(path, alpha=0.3)
# plot average path
    average_path = compute_average_path(price_paths)
    plt.plot(average_path, color='black', linewidth=2, label='Average Path')

    plt.title("Monte Carlo GBM Price Simulation")
    plt.xlabel("Days")
    plt.ylabel("Price (€)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
