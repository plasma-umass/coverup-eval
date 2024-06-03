# file pymonet/maybe.py:44-58
# lines [54, 55, 56, 57]
# branches ['54->55', '54->56']

import pytest
from pymonet.maybe import Maybe

def test_maybe_map_nothing(mocker):
    # Create a mock for the mapper function
    mapper = mocker.Mock(return_value=None)
    
    # Create a Maybe instance that is nothing
    maybe_nothing = Maybe.nothing()
    
    # Call the map method on the Maybe instance
    result = maybe_nothing.map(mapper)
    
    # Assert that the result is also a Maybe instance that is nothing
    assert result.is_nothing
    
    # Assert that the mapper function was not called
    mapper.assert_not_called()

def test_maybe_map_just(mocker):
    # Create a mock for the mapper function
    mapper = mocker.Mock(return_value=10)
    
    # Create a Maybe instance with a value
    maybe_just = Maybe.just(5)
    
    # Call the map method on the Maybe instance
    result = maybe_just.map(mapper)
    
    # Assert that the result is a Maybe instance with the mapped value
    assert not result.is_nothing
    assert result.value == 10
    
    # Assert that the mapper function was called once with the correct argument
    mapper.assert_called_once_with(5)
