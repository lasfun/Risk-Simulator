import pytest
from project_risk_simulator import calculate_metrics, compute_average_path

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