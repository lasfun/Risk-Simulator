# Risk Simulator: Financial Forecasting with GBM
**Video Demo: <URL>**
## Project Overview
The Risk Simulator is a Python-based command-line tool that forecasts future price movements of financial assets using historical market data and stochastic modeling. By applying Geometric Brownian Motion (GBM) and Monte Carlo simulation, the program generates multiple possible price paths and quantifies downside risk using statistical metrics.

This project was developed as part of CS50 and is also intended as a portfolio project demonstrating applied probability, data analysis, and Python programming.

## Quick Start

**Requirements**

`pip install yfinance matplotlib`

**Run the Program**

`python risk_simulator.py`

You will be prompted to enter:

- a ticker symbol (e.g., AAPL)
- a time horizon in days
- the number of Monte Carlo simulations

The program prints summary statistics in the terminal and plots simulated price paths.

## How It Works

The project follows a four-stage pipeline:

### 1. Data Acquisition
The program uses the yfinance API to fetch:

- most recent closing price (used as initial price) 
- one year of historical data (≈252 trading days) for parameter estimation

### 2. Parameter Estimation

From historical daily returns, the following parameters are calculated:
- Drift ($\mu$): Average daily return, annualized using 252 trading days.
- Volatility ($\sigma$): Standard deviation of daily returns, annualized.

### 3. Monte Carlo Price Simulation

Price evolution is modeled using Geometric Brownian Motion (GBM).
Each simulation applies the discretized GBM formula:

$$S_{t+1} = S_t \cdot \exp\left(\left(\mu - \frac{1}{2}\sigma^2\right)\Delta t + \sigma \sqrt{\Delta t} \cdot Z_t\right)$$

where $Z_t$ is a standard normal random variable.
This process is repeated across many independent simulations to generate a distribution of possible future prices.
### 4. Risk Metrics and Analysis
From the distribution of final simulated prices, the program computes:

- Minimum final price
- Maximum final price
- Average final price
- Value at Risk (VaR) at the 95% confidence level defined as the 5th percentile of final prices

These metrics provide a quantitative estimate of downside risk over the selected time horizon.
### 5. Visualization
The program plots a subset of simulated price paths using matplotlib, allowing the user to visually assess volatility and dispersion. On top of that an avarage path is computed and plotted to give a better overview.
## Project Structure and Functions
- `get_live_price`: Fetches the most recent closing price.
- `get_historical_parameters`: Computes drift and volatility from historical data.
- `simulate_single_path`: Generates one GBM price path.
- `monte_carlo_simulation`: Runs multiple independent simulations.
- `calculate_metrics`: Computes summary statistics and Value at Risk.
- `compute_average_path`: Computes an average path for plotting.
- `plot_prices`: Visualizes simulated price paths.
## Assumptions and Limitations
Assumes constant drift and volatility
Prices follow a log-normal distribution
No dividends, transaction costs, or jumps
Results are probabilistic, not predictive
This project is intended for educational purposes only and is not financial advice.
## Dependencies
`yfinance`
`matplotlib`