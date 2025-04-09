# file pymonet/lazy.py:27-36
# lines [27, 31, 32, 33, 34, 35]
# branches []

import pytest
from pymonet.lazy import Lazy

def test_lazy_eq(mocker):
    # Mock the constructor function to ensure it is the same for comparison
    constructor_fn = mocker.Mock(return_value=42)

    # Create two Lazy instances with the same constructor function and value
    lazy_value_1 = Lazy(constructor_fn)
    lazy_value_2 = Lazy(constructor_fn)
    lazy_value_1.value = 42
    lazy_value_2.value = 42
    lazy_value_1.is_evaluated = True
    lazy_value_2.is_evaluated = True

    # Create a third Lazy instance with a different constructor function
    lazy_value_3 = Lazy(mocker.Mock(return_value=42))
    lazy_value_3.value = 42
    lazy_value_3.is_evaluated = True

    # Create a fourth Lazy instance with a different value
    lazy_value_4 = Lazy(constructor_fn)
    lazy_value_4.value = 43
    lazy_value_4.is_evaluated = True

    # Create a fifth Lazy instance that is not evaluated
    lazy_value_5 = Lazy(constructor_fn)

    # Create a non-Lazy object
    non_lazy = object()

    # Assert that the first two Lazy instances are equal
    assert lazy_value_1 == lazy_value_2

    # Assert that the first Lazy instance is not equal to the third (different constructor)
    assert not (lazy_value_1 == lazy_value_3)

    # Assert that the first Lazy instance is not equal to the fourth (different value)
    assert not (lazy_value_1 == lazy_value_4)

    # Assert that the first Lazy instance is not equal to the fifth (not evaluated)
    assert not (lazy_value_1 == lazy_value_5)

    # Assert that the Lazy instance is not equal to a non-Lazy object
    assert not (lazy_value_1 == non_lazy)
