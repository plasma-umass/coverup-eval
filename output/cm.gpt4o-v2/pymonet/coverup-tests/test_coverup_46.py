# file: pymonet/lazy.py:106-115
# asked: {"lines": [106, 113, 115], "branches": []}
# gained: {"lines": [106, 113, 115], "branches": []}

import pytest
from pymonet.lazy import Lazy
from pymonet.box import Box

def test_lazy_to_box():
    # Arrange
    def constructor_fn(x):
        return x * 2

    lazy_instance = Lazy(constructor_fn)
    
    # Act
    box_instance = lazy_instance.to_box(5)
    
    # Assert
    assert isinstance(box_instance, Box)
    assert box_instance.value == 10
