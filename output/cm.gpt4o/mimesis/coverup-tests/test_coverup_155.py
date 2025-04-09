# file mimesis/random.py:97-105
# lines [97, 105]
# branches []

import pytest
from mimesis.random import Random

def test_random_uniform(mocker):
    # Mock the random method to control the output
    mock_random = mocker.patch('random.Random.random', return_value=0.5)
    
    rnd = Random()
    
    # Test with default precision
    result = rnd.uniform(1.0, 2.0)
    assert result == 1.5, f"Expected 1.5 but got {result}"
    
    # Test with custom precision
    result = rnd.uniform(1.0, 2.0, precision=2)
    assert result == 1.50, f"Expected 1.50 but got {result}"
    
    # Test with different range
    result = rnd.uniform(10.0, 20.0)
    assert result == 15.0, f"Expected 15.0 but got {result}"
    
    # Test with different random value
    mock_random.return_value = 0.25
    result = rnd.uniform(1.0, 2.0)
    assert result == 1.25, f"Expected 1.25 but got {result}"
    
    # Test with negative range
    mock_random.return_value = 0.5
    result = rnd.uniform(-1.0, 1.0)
    assert result == 0.0, f"Expected 0.0 but got {result}"
    
    # Test with zero range
    result = rnd.uniform(0.0, 0.0)
    assert result == 0.0, f"Expected 0.0 but got {result}"
