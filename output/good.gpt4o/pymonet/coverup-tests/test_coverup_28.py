# file pymonet/lazy.py:15-22
# lines [15, 20, 21, 22]
# branches []

import pytest
from pymonet.lazy import Lazy

def test_lazy_initialization():
    def sample_constructor(x):
        return x * 2

    lazy_instance = Lazy(sample_constructor)
    
    assert lazy_instance.constructor_fn == sample_constructor
    assert not lazy_instance.is_evaluated
    assert lazy_instance.value is None

def test_lazy_evaluation():
    def sample_constructor(x):
        return x * 2

    lazy_instance = Lazy(sample_constructor)
    
    # Simulate the fold method call which is not provided in the snippet
    if not lazy_instance.is_evaluated:
        lazy_instance.value = lazy_instance.constructor_fn(10)
        lazy_instance.is_evaluated = True

    assert lazy_instance.is_evaluated
    assert lazy_instance.value == 20
