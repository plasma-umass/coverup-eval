# file: pymonet/box.py:20-21
# asked: {"lines": [20, 21], "branches": []}
# gained: {"lines": [20, 21], "branches": []}

import pytest
from pymonet.box import Box

def test_box_eq_with_same_value():
    box1 = Box(10)
    box2 = Box(10)
    assert box1 == box2

def test_box_eq_with_different_value():
    box1 = Box(10)
    box2 = Box(20)
    assert box1 != box2

def test_box_eq_with_non_box():
    box = Box(10)
    assert box != 10

def test_box_eq_with_same_box():
    box = Box(10)
    assert box == box
