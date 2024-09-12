# file: pymonet/box.py:81-90
# asked: {"lines": [81, 88, 90], "branches": []}
# gained: {"lines": [81, 88, 90], "branches": []}

import pytest
from pymonet.box import Box
from pymonet.lazy import Lazy

def test_box_to_lazy():
    # Create a Box instance with a sample value
    box = Box(42)
    
    # Convert the Box to a Lazy
    lazy = box.to_lazy()
    
    # Assert that the returned object is an instance of Lazy
    assert isinstance(lazy, Lazy)
    
    # Assert that the Lazy object, when evaluated, returns the original Box value
    assert lazy.constructor_fn() == 42
