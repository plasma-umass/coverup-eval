# file: pymonet/lazy.py:38-48
# asked: {"lines": [38, 39, 48], "branches": []}
# gained: {"lines": [38, 39, 48], "branches": []}

import pytest
from pymonet.lazy import Lazy

def test_lazy_of():
    value = 42
    lazy_instance = Lazy.of(value)
    
    assert isinstance(lazy_instance, Lazy)
    assert lazy_instance.constructor_fn() == value
