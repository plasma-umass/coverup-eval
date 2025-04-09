# file pymonet/either.py:88-95
# lines [88, 95]
# branches []

import pytest
from pymonet.either import Left

def test_left_map_does_not_apply_function():
    # Create a Left instance with a value
    left_value = Left('error')

    # Define a function that we will pass to the map method
    def should_not_be_called(value):
        raise Exception("This function should not be called")

    # Call the map method with the function that should not be called
    result = left_value.map(should_not_be_called)

    # Assert that the result is still a Left instance
    assert isinstance(result, Left)

    # Assert that the value inside the Left instance has not changed
    assert result.value == 'error'
