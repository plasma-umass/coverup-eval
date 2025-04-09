# file flutes/iterator.py:340-341
# lines [340, 341]
# branches []

import pytest
from flutes.iterator import Range

def test_range_length():
    # Create an instance of the Range class with a specific length
    start = 0
    end = 5
    range_instance = Range(start, end)

    # Calculate the expected length
    expected_length = end - start

    # Assert that the __len__ method returns the correct length
    assert len(range_instance) == expected_length

    # Clean up is not necessary as we are not modifying any shared state outside the test
