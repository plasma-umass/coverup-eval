# file: f020/__init__.py:4-21
# asked: {"lines": [4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}
# gained: {"lines": [4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}

import pytest
from f020 import find_closest_elements

def test_find_closest_elements():
    # Test with a list of numbers
    numbers = [4.0, 1.0, 7.0, 3.0]
    result = find_closest_elements(numbers)
    assert result == (3.0, 4.0), f"Expected (3.0, 4.0) but got {result}"

    # Test with a list containing negative numbers
    numbers = [-1.0, -4.0, -2.0, -3.0]
    result = find_closest_elements(numbers)
    assert result == (-2.0, -1.0), f"Expected (-2.0, -1.0) but got {result}"

    # Test with a list containing duplicate numbers
    numbers = [1.0, 2.0, 2.0, 3.0]
    result = find_closest_elements(numbers)
    assert result == (2.0, 2.0), f"Expected (2.0, 2.0) but got {result}"

    # Test with a list containing only two numbers
    numbers = [5.0, 10.0]
    result = find_closest_elements(numbers)
    assert result == (5.0, 10.0), f"Expected (5.0, 10.0) but got {result}"

    # Test with a list containing one number
    numbers = [5.0]
    result = find_closest_elements(numbers)
    assert result is None, f"Expected None but got {result}"

    # Test with an empty list
    numbers = []
    result = find_closest_elements(numbers)
    assert result is None, f"Expected None but got {result}"
