# file flutes/iterator.py:164-165
# lines [164, 165]
# branches []

import pytest
from flutes.iterator import scanl
from typing import List

def test_scanl():
    # Define a simple addition function for testing
    def add(x, y):
        return x + y

    # Create an iterable for testing
    test_iterable = [1, 2, 3, 4]

    # Initial value for the scanl function
    initial_value = 10

    # Expected result after applying scanl with add function
    expected_result = [10, 11, 13, 16, 20]

    # Call the scanl function with the test data
    result = list(scanl(add, test_iterable, initial_value))

    # Assert that the result matches the expected result
    assert result == expected_result

    # Clean up is not necessary as the test does not affect external state or resources
