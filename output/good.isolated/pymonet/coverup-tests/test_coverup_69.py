# file pymonet/maybe.py:35-42
# lines [35, 36, 42]
# branches []

import pytest
from pymonet.maybe import Maybe

def test_maybe_nothing():
    # Test the Maybe.nothing() class method
    result = Maybe.nothing()
    
    # Assert that the result is an instance of Maybe
    assert isinstance(result, Maybe)
    
    # Assert that the result is indeed a 'nothing' value
    assert result.is_nothing is True
    
    # Assert that the value of the result is None
    assert result.get_or_else(None) is None
