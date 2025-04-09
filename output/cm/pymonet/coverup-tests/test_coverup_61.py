# file pymonet/box.py:23-24
# lines [23, 24]
# branches []

import pytest
from pymonet.box import Box

def test_box_str():
    box = Box(10)
    assert str(box) == 'Box[value=10]'
