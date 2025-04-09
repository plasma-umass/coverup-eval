# file: pymonet/lazy.py:27-36
# asked: {"lines": [27, 31, 32, 33, 34, 35], "branches": []}
# gained: {"lines": [27, 31, 32, 33, 34, 35], "branches": []}

import pytest
from pymonet.lazy import Lazy

def test_lazy_eq_same_instance():
    constructor_fn = lambda x: x + 1
    lazy1 = Lazy(constructor_fn)
    lazy2 = lazy1
    assert lazy1 == lazy2

def test_lazy_eq_different_instance_same_values():
    constructor_fn = lambda x: x + 1
    lazy1 = Lazy(constructor_fn)
    lazy2 = Lazy(constructor_fn)
    lazy1.is_evaluated = True
    lazy1.value = 42
    lazy2.is_evaluated = True
    lazy2.value = 42
    assert lazy1 == lazy2

def test_lazy_eq_different_instance_different_values():
    constructor_fn1 = lambda x: x + 1
    constructor_fn2 = lambda x: x + 2
    lazy1 = Lazy(constructor_fn1)
    lazy2 = Lazy(constructor_fn2)
    lazy1.is_evaluated = True
    lazy1.value = 42
    lazy2.is_evaluated = True
    lazy2.value = 43
    assert lazy1 != lazy2

def test_lazy_eq_different_type():
    constructor_fn = lambda x: x + 1
    lazy = Lazy(constructor_fn)
    assert lazy != 42
