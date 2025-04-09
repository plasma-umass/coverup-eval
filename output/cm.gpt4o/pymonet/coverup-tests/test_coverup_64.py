# file pymonet/box.py:23-24
# lines [23, 24]
# branches []

import pytest
from pymonet.box import Box

def test_box_str():
    class TestBox(Box):
        def __init__(self, value):
            self.value = value

    test_value = 42
    box = TestBox(test_value)
    assert str(box) == f'Box[value={test_value}]'
