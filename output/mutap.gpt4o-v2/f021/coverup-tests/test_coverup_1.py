# file: f021/__init__.py:4-8
# asked: {"lines": [4, 6, 7, 8], "branches": []}
# gained: {"lines": [4, 6, 7, 8], "branches": []}

import pytest
from f021 import rescale_to_unit

def test_rescale_to_unit():
    # Test with a list of positive numbers
    numbers = [2.0, 4.0, 6.0, 8.0]
    expected = [0.0, 0.3333333333333333, 0.6666666666666666, 1.0]
    result = rescale_to_unit(numbers)
    assert result == expected

    # Test with a list of negative numbers
    numbers = [-8.0, -6.0, -4.0, -2.0]
    expected = [0.0, 0.3333333333333333, 0.6666666666666666, 1.0]
    result = rescale_to_unit(numbers)
    assert result == expected

    # Test with a list of mixed positive and negative numbers
    numbers = [-3.0, -1.0, 1.0, 3.0]
    expected = [0.0, 0.3333333333333333, 0.6666666666666666, 1.0]
    result = rescale_to_unit(numbers)
    assert result == expected

    # Test with a list containing the same number
    numbers = [5.0, 5.0, 5.0, 5.0]
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit(numbers)

    # Test with an empty list
    numbers = []
    with pytest.raises(ValueError):
        rescale_to_unit(numbers)
