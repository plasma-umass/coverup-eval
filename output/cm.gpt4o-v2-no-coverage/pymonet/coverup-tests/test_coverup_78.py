# file: pymonet/box.py:59-68
# asked: {"lines": [59, 66, 68], "branches": []}
# gained: {"lines": [59, 66, 68], "branches": []}

import pytest
from pymonet.box import Box
from pymonet.maybe import Maybe

def test_box_to_maybe():
    # Create a Box instance with a value
    box = Box(42)
    
    # Transform Box to Maybe
    maybe = box.to_maybe()
    
    # Assert that the Maybe instance is not empty and contains the correct value
    assert isinstance(maybe, Maybe)
    assert maybe.value == 42
    assert not maybe.is_nothing
