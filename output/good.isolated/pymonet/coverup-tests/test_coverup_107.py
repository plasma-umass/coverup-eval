# file pymonet/box.py:20-21
# lines [20, 21]
# branches []

import pytest
from pymonet.box import Box

def test_box_equality():
    box1 = Box(10)
    box2 = Box(10)
    box3 = Box(20)
    non_box = "not_a_box"

    assert box1 == box2, "Two boxes with the same value should be equal"
    assert not (box1 == box3), "Two boxes with different values should not be equal"
    assert not (box1 == non_box), "A box should not be equal to a non-box object"

def test_box_inequality():
    box1 = Box(10)
    box2 = Box(10)
    box3 = Box(20)
    non_box = "not_a_box"

    assert not (box1 != box2), "Two boxes with the same value should not be unequal"
    assert box1 != box3, "Two boxes with different values should be unequal"
    assert box1 != non_box, "A box should be unequal to a non-box object"
