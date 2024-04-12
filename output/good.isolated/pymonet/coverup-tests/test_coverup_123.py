# file pymonet/maybe.py:127-138
# lines [134, 136, 137, 138]
# branches ['136->137', '136->138']

import pytest
from pymonet.maybe import Maybe
from pymonet.box import Box

def test_maybe_to_box_with_nothing():
    # Create a Maybe instance representing Nothing
    maybe_nothing = Maybe.nothing()
    
    # Call to_box on the Maybe instance
    result = maybe_nothing.to_box()
    
    # Assert that the result is an instance of Box
    assert isinstance(result, Box)
    
    # Assert that the result contains None
    assert result.value is None

def test_maybe_to_box_with_just():
    # Create a Maybe instance with a value
    maybe_just = Maybe.just('test_value')
    
    # Call to_box on the Maybe instance
    result = maybe_just.to_box()
    
    # Assert that the result is an instance of Box
    assert isinstance(result, Box)
    
    # Assert that the result contains the correct value
    assert result.value == 'test_value'
