# file: pymonet/lazy.py:80-93
# asked: {"lines": [80, 89, 90, 91, 93], "branches": []}
# gained: {"lines": [80, 89, 90, 91, 93], "branches": []}

import pytest
from pymonet.lazy import Lazy

def test_lazy_bind():
    # Mock function to be used with bind
    def mock_fn(x):
        return Lazy(lambda: x + 1)

    # Create a Lazy instance with a simple constructor function
    lazy_instance = Lazy(lambda: 5)

    # Bind the mock function to the lazy instance
    bound_instance = lazy_instance.bind(mock_fn)

    # Assert that the bound instance is a Lazy instance
    assert isinstance(bound_instance, Lazy)

    # Compute the value using the bound instance's constructor function
    computed_value = bound_instance.constructor_fn()

    # Assert that the computed value is a function
    assert callable(computed_value)

    # Assert that the computed value returns the expected result when called
    assert computed_value() == 6
