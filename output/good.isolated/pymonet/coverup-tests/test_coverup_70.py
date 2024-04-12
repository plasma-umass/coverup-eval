# file pymonet/maybe.py:44-58
# lines [44, 54, 55, 56, 57]
# branches ['54->55', '54->56']

import pytest
from pymonet.maybe import Maybe

def test_maybe_map_with_nothing():
    # Create a Maybe instance with no value
    maybe_instance = Maybe.nothing()
    
    # Define a mapper function that should not be called
    def mapper(x):
        return x * 2
    
    # Call the map method
    result = maybe_instance.map(mapper)
    
    # Assert that the result is a Maybe instance with no value
    assert isinstance(result, Maybe)
    assert result.is_nothing

def test_maybe_map_with_just():
    # Create a Maybe instance with a value
    maybe_instance = Maybe.just(10)
    
    # Define a mapper function
    def mapper(x):
        return x * 2
    
    # Call the map method
    result = maybe_instance.map(mapper)
    
    # Assert that the result is a Maybe instance with the mapped value
    assert isinstance(result, Maybe)
    assert not result.is_nothing
    assert result.value == 20
