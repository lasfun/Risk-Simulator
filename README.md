# Risk Simulator: Financial Forecasting with GBM

### Video Demo: <URL>

## Project Overview

The **Risk Simulator** is a Python-based command-line tool designed to forecast the future price movements of financial assets. By leveraging real-world market data and stochastic modeling, it allows users to visualize potential price volatility and quantify risk through statistical metrics.

## Detailed Description

The project follows a four-stage pipeline: **Data acquisition**, **Parameter Estimation**, **Simulation**, and **Visualization**.

**1. Data Integration**
The tool uses the yfinance API to fetch live data. Instead of requiring the user to enter current prices or volatility, the program automatically downloads the last 252 trading days (one year) of historical data for any given ticker symbol. 

**2. Financial Logic & Mathematical Modelling**
The core engine of the simulation is based on the Geometric Brownian Motion (**GBM**). Financial markets are rarely predictable, but GBM provides a mathematically sound way to model random walks with a drift.

The simulation uses the following stochastic differential equation: 

$dS_t =  \mu S_t dt + \sigma S_t dW_t$

In this implementation:

**Drift(\mu)** : Calculated as the annualized average daily return of the asset.

**Volatility(\sigma)**: Derived from the standard deviation of historical returns.

**Wiener Process(W_t)**: Generated using Python's `random.gauss(0, 1)` to simulate daily market shocks.

## Risk Metrics and Analysis
Beyond just plotting a line, this program calculates the Value at Risk (**VaR**). By analyzing the simulated path, the tool identifies the "worst-case-scenario" at a 95% confidence level, helping a user understand how much capital might be at risk over the chosen time horizon.


### Project Structures and Functions

`get_live_prices`: Connects to the Yahoo Finance API to retrieve the most recent closing price.

`get_historical_parameter`: Performs the statistical heavy lifting by calculating volatility and drift. 

`simulate_prices`: The iterative loop that applies the GBM formula for each day in the time horizon.

`calculate_metrics`: Calculates Minimum, Maximum, Average and VaR from the resulting data.

`plot_prices`: Plots the graph of the simulated price path using `matplotlib`.

#### Requirements:

To run this project you must install the following dependencies:

`yfinance`
`matplotlib`