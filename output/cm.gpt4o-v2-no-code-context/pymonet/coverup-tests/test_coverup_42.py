# file: pymonet/box.py:70-79
# asked: {"lines": [70, 77, 79], "branches": []}
# gained: {"lines": [70, 77, 79], "branches": []}

import pytest
from pymonet.box import Box
from pymonet.either import Right

def test_box_to_either():
    box = Box(42)
    either = box.to_either()
    
    assert isinstance(either, Right)
    assert either.value == 42
