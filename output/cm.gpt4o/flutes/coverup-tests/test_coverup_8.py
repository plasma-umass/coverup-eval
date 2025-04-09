# file flutes/iterator.py:160-161
# lines [160, 161]
# branches []

import pytest
from flutes.iterator import scanl

def test_scanl():
    # Define a simple function to use with scanl
    def add(x, y):
        return x + y

    # Create an iterable
    iterable = [1, 2, 3, 4]

    # Use scanl with the add function and the iterable
    result = list(scanl(add, iterable))

    # Verify the result
    assert result == [1, 3, 6, 10]

    # Clean up (not necessary in this case as no external resources are used)

