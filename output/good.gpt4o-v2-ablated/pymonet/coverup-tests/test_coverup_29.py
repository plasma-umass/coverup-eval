# file: pymonet/lazy.py:15-22
# asked: {"lines": [15, 20, 21, 22], "branches": []}
# gained: {"lines": [15, 20, 21, 22], "branches": []}

import pytest
from pymonet.lazy import Lazy

def test_lazy_initialization():
    def constructor_fn(x):
        return x * 2

    lazy_instance = Lazy(constructor_fn)
    assert lazy_instance.constructor_fn == constructor_fn
    assert not lazy_instance.is_evaluated
    assert lazy_instance.value is None

def test_lazy_evaluation():
    def constructor_fn(x):
        return x * 2

    lazy_instance = Lazy(constructor_fn)
    result = lazy_instance.constructor_fn(5)
    assert result == 10

    lazy_instance.is_evaluated = True
    lazy_instance.value = result
    assert lazy_instance.is_evaluated
    assert lazy_instance.value == 10
