# file: pymonet/lazy.py:68-78
# asked: {"lines": [68, 78], "branches": []}
# gained: {"lines": [68, 78], "branches": []}

import pytest
from pymonet.lazy import Lazy

def test_lazy_ap():
    # Create a Lazy instance with a simple constructor function
    lazy_value = Lazy(lambda x: x + 1)
    
    # Create an applicative Lazy instance with a function
    applicative = Lazy(lambda x: x * 2)
    
    # Apply the applicative to the lazy_value
    result = lazy_value.ap(applicative)
    
    # Assert that the result is a Lazy instance
    assert isinstance(result, Lazy)
    
    # Assert that the result's constructor function works as expected
    assert result.constructor_fn(3) == 7  # (3 * 2) + 1

    # Clean up
    del lazy_value
    del applicative
    del result
