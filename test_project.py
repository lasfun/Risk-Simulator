import pytest
from project_risk_simulator import calculate_metrics, simulate_prices

def test_calculate_metrics():
    # tests the calculation of max, min, average and VaR
    prices = [10.0, 20.0, 30.0, 40.0, 50.0]
    max_p, min_p, avg_p, var_95 = calculate_metrics(prices)
    assert max_p == 50.0
    assert min_p == 10.0
    assert avg_p == 30.0
    assert var_95 == 10.0 # 5% quantile should be smallest with 5 data points

def test_simulation_length():
    # Checks if the number of simulated days is correct
    days = 365
    prices = simulate_prices(100, days, 0.2, 0.05)
    assert len(prices) == days + 1