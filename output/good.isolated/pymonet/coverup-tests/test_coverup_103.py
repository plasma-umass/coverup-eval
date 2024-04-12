# file pymonet/maybe.py:87-99
# lines [87, 97, 98, 99]
# branches ['97->98', '97->99']

import pytest
from pymonet.maybe import Maybe

def test_maybe_filter_returns_nothing_when_empty():
    # Create a Maybe instance that is empty
    maybe_instance = Maybe.nothing()
    
    # Define a filter function that would return True if called
    filterer = lambda x: True
    
    # Call the filter method
    result = maybe_instance.filter(filterer)
    
    # Assert that the result is an empty Maybe
    assert result.is_nothing is True

def test_maybe_filter_returns_nothing_when_filterer_returns_false():
    # Create a Maybe instance with a value
    maybe_instance = Maybe.just(10)
    
    # Define a filter function that returns False
    filterer = lambda x: False
    
    # Call the filter method
    result = maybe_instance.filter(filterer)
    
    # Assert that the result is an empty Maybe
    assert result.is_nothing is True

def test_maybe_filter_returns_just_when_filterer_returns_true():
    # Create a Maybe instance with a value
    maybe_instance = Maybe.just(10)
    
    # Define a filter function that returns True
    filterer = lambda x: True
    
    # Call the filter method
    result = maybe_instance.filter(filterer)
    
    # Assert that the result is a Maybe with the same value
    assert result.is_nothing is False
    assert result.value == 10
