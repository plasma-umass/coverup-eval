# file: f004/__init__.py:4-7
# asked: {"lines": [4, 6, 7], "branches": []}
# gained: {"lines": [4, 6, 7], "branches": []}

import pytest
from f004 import mean_absolute_deviation

def test_mean_absolute_deviation():
    # Test with a list of positive numbers
    numbers = [1, 2, 3, 4, 5]
    result = mean_absolute_deviation(numbers)
    expected = 1.2
    assert result == pytest.approx(expected), f"Expected {expected}, got {result}"

    # Test with a list of negative numbers
    numbers = [-1, -2, -3, -4, -5]
    result = mean_absolute_deviation(numbers)
    expected = 1.2
    assert result == pytest.approx(expected), f"Expected {expected}, got {result}"

    # Test with a list of mixed positive and negative numbers
    numbers = [-1, -2, 3, 4, 5]
    result = mean_absolute_deviation(numbers)
    expected = 2.64
    assert result == pytest.approx(expected), f"Expected {expected}, got {result}"

    # Test with a list containing zero
    numbers = [0, 0, 0, 0, 0]
    result = mean_absolute_deviation(numbers)
    expected = 0.0
    assert result == pytest.approx(expected), f"Expected {expected}, got {result}"

    # Test with a single element list
    numbers = [5]
    result = mean_absolute_deviation(numbers)
    expected = 0.0
    assert result == pytest.approx(expected), f"Expected {expected}, got {result}"

    # Test with an empty list
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])

