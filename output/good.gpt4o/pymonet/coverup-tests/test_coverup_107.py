# file pymonet/lazy.py:56-66
# lines [66]
# branches []

import pytest
from pymonet.lazy import Lazy

def test_lazy_map():
    # Define a constructor function for the Lazy instance
    def constructor_fn(x):
        return x + 1

    # Create a Lazy instance
    lazy_instance = Lazy(constructor_fn)

    # Define a mapper function
    def mapper_fn(y):
        return y * 2

    # Use the map method to create a new Lazy instance
    mapped_lazy_instance = lazy_instance.map(mapper_fn)

    # Verify that the new Lazy instance is created correctly
    assert isinstance(mapped_lazy_instance, Lazy)

    # Verify that the constructor function and mapper function work as expected
    assert mapped_lazy_instance.constructor_fn(3) == 8  # (3 + 1) * 2 = 8
