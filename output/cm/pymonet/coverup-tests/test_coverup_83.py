# file pymonet/maybe.py:60-71
# lines [60, 69, 70, 71]
# branches ['69->70', '69->71']

import pytest
from pymonet.maybe import Maybe
from unittest.mock import Mock

def test_maybe_bind_with_nothing():
    # Create a Maybe instance that is nothing
    maybe_instance = Maybe.nothing()
    
    # Define a mapper function that should not be called
    mapper = Mock()
    
    # Call bind on the Maybe instance with the mapper
    result = maybe_instance.bind(mapper)
    
    # Assert that the result is a Maybe instance with no value
    assert isinstance(result, Maybe)
    assert result.is_nothing
    
    # Assert that the mapper was not called
    mapper.assert_not_called()

def test_maybe_bind_with_value():
    # Create a Maybe instance with a value
    maybe_instance = Maybe.just(5)
    
    # Define a mapper function that returns a Maybe instance
    def mapper(value):
        return Maybe.just(value * 2)
    
    # Call bind on the Maybe instance with the mapper
    result = maybe_instance.bind(mapper)
    
    # Assert that the result is a Maybe instance with the mapped value
    assert isinstance(result, Maybe)
    assert not result.is_nothing
    assert result.value == 10
