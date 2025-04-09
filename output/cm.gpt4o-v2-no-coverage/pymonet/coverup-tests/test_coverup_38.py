# file: pymonet/lazy.py:15-22
# asked: {"lines": [15, 20, 21, 22], "branches": []}
# gained: {"lines": [15, 20, 21, 22], "branches": []}

import pytest
from pymonet.lazy import Lazy

def test_lazy_init():
    def dummy_constructor(x):
        return x * 2

    lazy_instance = Lazy(dummy_constructor)
    
    assert lazy_instance.constructor_fn == dummy_constructor
    assert not lazy_instance.is_evaluated
    assert lazy_instance.value is None
