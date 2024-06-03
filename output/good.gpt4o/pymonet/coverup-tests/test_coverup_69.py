# file pymonet/box.py:20-21
# lines [20, 21]
# branches []

import pytest
from pymonet.box import Box

def test_box_equality():
    box1 = Box(10)
    box2 = Box(10)
    box3 = Box(20)
    non_box = 10

    # Test equality with another Box with the same value
    assert box1 == box2

    # Test inequality with another Box with a different value
    assert box1 != box3

    # Test inequality with a non-Box object
    assert box1 != non_box
