# file mimesis/providers/numbers.py:34-45
# lines [34, 35, 45]
# branches []

import pytest
from mimesis.providers.numbers import Numbers

@pytest.fixture
def numbers_provider():
    return Numbers()

def test_floats(numbers_provider):
    start = 5.0
    end = 10.0
    n = 5
    precision = 2
    result = numbers_provider.floats(start=start, end=end, n=n, precision=precision)
    
    assert len(result) == n, "The length of the result list should be equal to n"
    assert all(start <= num <= end for num in result), "All numbers should be within the specified range"
    assert all(isinstance(num, float) for num in result), "All elements should be of type float"
    assert all(round(num, precision) == num for num in result), "All numbers should have the specified precision"

    # Clean up is not necessary as the test does not modify any external state
