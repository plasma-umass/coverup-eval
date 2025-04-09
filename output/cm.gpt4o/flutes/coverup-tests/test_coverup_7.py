# file flutes/iterator.py:164-165
# lines [164, 165]
# branches []

import pytest
from flutes.iterator import scanl

def test_scanl():
    # Define a simple function to use with scanl
    def add(x, y):
        return x + y

    # Create an iterable
    iterable = [1, 2, 3, 4]

    # Call scanl with the function, iterable, and an initial value
    result = list(scanl(add, iterable, 0))

    # Verify the result
    assert result == [0, 1, 3, 6, 10]

    # Test with a different initial value
    result = list(scanl(add, iterable, 10))
    assert result == [10, 11, 13, 16, 20]

    # Test with an empty iterable
    result = list(scanl(add, [], 5))
    assert result == [5]

    # Test with a different function
    def multiply(x, y):
        return x * y

    result = list(scanl(multiply, iterable, 1))
    assert result == [1, 1, 2, 6, 24]

    # Test with a single element iterable
    result = list(scanl(add, [5], 2))
    assert result == [2, 7]
