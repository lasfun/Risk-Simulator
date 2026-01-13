# Energy Risk Simulator

#### Video Demo: <URL zu deinem Video später einfügen>

## Description
This project is a **Monte Carlo Simulation** tool designed to forecast potential price developments for financial assets or energy commodities. 

### Financial Logic
The simulator uses **Geometric Brownian Motion (GBM)** to project future price paths. GBM is a continuous-time stochastic process where the logarithm of the randomly varying quantity follows a Brownian motion with drift.

Formula: $dS_t = \mu S_t dt + \sigma S_t dW_t$

### Features
- **Live Data:** Integration of `yfinance` to fetch the latest market prices.
- **Statistical Parameters:** Calculation of historical volatility and drift from the past 252 trading days.
- **Risk Metrics:** Calculation of the **Value at Risk (VaR)** at a 95% confidence level.
- **Visualization:** A graphical representation of the simulated price path using `matplotlib`.

## Installation
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the application: `python Energy_Risk_Simulator.py`.