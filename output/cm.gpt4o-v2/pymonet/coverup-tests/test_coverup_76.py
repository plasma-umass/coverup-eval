# file: pymonet/lazy.py:56-66
# asked: {"lines": [56, 66], "branches": []}
# gained: {"lines": [56, 66], "branches": []}

import pytest
from pymonet.lazy import Lazy

def test_lazy_map():
    # Arrange
    def constructor_fn(x):
        return x + 1

    def mapper_fn(y):
        return y * 2

    lazy_instance = Lazy(constructor_fn)

    # Act
    mapped_lazy = lazy_instance.map(mapper_fn)
    result = mapped_lazy.constructor_fn(3)

    # Assert
    assert result == 8  # (3 + 1) * 2

    # Clean up
    del lazy_instance
    del mapped_lazy
