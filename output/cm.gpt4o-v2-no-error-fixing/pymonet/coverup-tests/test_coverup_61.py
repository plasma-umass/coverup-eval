# file: pymonet/lazy.py:56-66
# asked: {"lines": [56, 66], "branches": []}
# gained: {"lines": [56, 66], "branches": []}

import pytest
from pymonet.lazy import Lazy

def test_lazy_map():
    # Mock constructor function
    constructor_fn = lambda: 10
    lazy_instance = Lazy(constructor_fn)
    
    # Mapper function
    mapper = lambda x: x * 2
    
    # Apply map
    new_lazy_instance = lazy_instance.map(mapper)
    
    # Assert the new Lazy instance is created
    assert isinstance(new_lazy_instance, Lazy)
    
    # Assert the mapped value is correct
    assert new_lazy_instance.constructor_fn() == 20
