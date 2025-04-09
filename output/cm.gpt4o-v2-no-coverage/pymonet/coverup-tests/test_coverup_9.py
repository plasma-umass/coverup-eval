# file: pymonet/lazy.py:27-36
# asked: {"lines": [27, 31, 32, 33, 34, 35], "branches": []}
# gained: {"lines": [27, 31, 32, 33, 34, 35], "branches": []}

import pytest
from pymonet.lazy import Lazy

def test_lazy_eq():
    def constructor_fn(x):
        return x + 1

    lazy1 = Lazy(constructor_fn)
    lazy2 = Lazy(constructor_fn)
    lazy3 = Lazy(lambda x: x + 2)

    # Test equality with same constructor function and unevaluated
    assert lazy1 == lazy2

    # Test inequality with different constructor function
    assert lazy1 != lazy3

    # Evaluate lazy1 and lazy2
    lazy1.value = constructor_fn(1)
    lazy1.is_evaluated = True
    lazy2.value = constructor_fn(1)
    lazy2.is_evaluated = True

    # Test equality with same constructor function and evaluated
    assert lazy1 == lazy2

    # Change value of lazy2
    lazy2.value = constructor_fn(2)

    # Test inequality with different values
    assert lazy1 != lazy2

    # Test inequality with different types
    assert lazy1 != "not a Lazy instance"
