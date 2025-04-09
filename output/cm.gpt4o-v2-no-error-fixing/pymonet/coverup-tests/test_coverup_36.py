# file: pymonet/lazy.py:50-54
# asked: {"lines": [50, 51, 52, 54], "branches": []}
# gained: {"lines": [50, 51, 52, 54], "branches": []}

import pytest
from pymonet.lazy import Lazy

def test_lazy_compute_value():
    def constructor_fn(x):
        return x * 2

    lazy_instance = Lazy(constructor_fn)
    
    result = lazy_instance._compute_value(5)
    
    assert lazy_instance.is_evaluated == True
    assert lazy_instance.value == 10
    assert result == 10
