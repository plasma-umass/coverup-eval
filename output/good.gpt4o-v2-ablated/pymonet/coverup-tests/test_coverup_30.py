# file: pymonet/lazy.py:38-48
# asked: {"lines": [38, 39, 48], "branches": []}
# gained: {"lines": [38, 39, 48], "branches": []}

import pytest
from pymonet.lazy import Lazy

def test_lazy_of():
    # Test that Lazy.of correctly wraps a value
    value = 42
    lazy_instance = Lazy.of(value)
    
    # Assert that the lazy_instance is an instance of Lazy
    assert isinstance(lazy_instance, Lazy)
    
    # Assert that the function inside lazy_instance returns the correct value
    assert lazy_instance.constructor_fn() == value
