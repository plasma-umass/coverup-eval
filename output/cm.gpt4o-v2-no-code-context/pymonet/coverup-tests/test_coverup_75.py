# file: pymonet/lazy.py:56-66
# asked: {"lines": [56, 66], "branches": []}
# gained: {"lines": [56, 66], "branches": []}

import pytest
from pymonet.lazy import Lazy

def test_lazy_map():
    # Arrange
    def constructor_fn(x):
        return x + 1

    lazy_instance = Lazy(constructor_fn)

    def mapper_fn(y):
        return y * 2

    # Act
    mapped_lazy_instance = lazy_instance.map(mapper_fn)

    # Assert
    assert isinstance(mapped_lazy_instance, Lazy)
    assert mapped_lazy_instance.constructor_fn(3) == 8  # (3 + 1) * 2

def test_lazy_map_with_different_mapper():
    # Arrange
    def constructor_fn(x):
        return x * 3

    lazy_instance = Lazy(constructor_fn)

    def mapper_fn(y):
        return y - 4

    # Act
    mapped_lazy_instance = lazy_instance.map(mapper_fn)

    # Assert
    assert isinstance(mapped_lazy_instance, Lazy)
    assert mapped_lazy_instance.constructor_fn(2) == 2  # (2 * 3) - 4

@pytest.fixture(autouse=True)
def cleanup():
    # Cleanup code if necessary
    yield
    # No state pollution to clean up in this case
