import pytest
import math

from project import calculate_metrics, compute_average_path, simulate_single_path

def test_calculate_metrics():
    test_data = [[0, 100], [0, 200]]
    result = calculate_metrics(test_data)
    
    assert result["average"] == 150
    assert result["min"] == 100
    assert result["max"] == 200
    assert result["var_95"] == 100

def test_compute_average_path():
    path1 = [10, 20, 30]
    path2 = [20, 40, 60]
    
    result = compute_average_path([path1, path2])
    assert result == [15.0, 30.0, 45.0]

def test_structure():

    test_data = [[10, 10], [20, 20]]
    result = calculate_metrics(test_data)
    assert isinstance(result, dict)
    assert "var_95" in result

def test_simulate_single_path_deterministic():
    start_price = 100
    days = 1
    volatility = 0  #eliminates randomness
    drift = 0.1     
    
    result = simulate_single_path(start_price, days, volatility, drift)
    
    # calculation with zero volatility:
    dt = 1/252
    expected_price = start_price * math.exp(drift * dt)
    
    assert len(result) == days + 1
    assert pytest.approx(result[1], rel=1e-5) == expected_price