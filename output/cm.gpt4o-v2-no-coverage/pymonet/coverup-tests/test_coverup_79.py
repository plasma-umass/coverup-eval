# file: pymonet/box.py:13-18
# asked: {"lines": [13, 18], "branches": []}
# gained: {"lines": [13, 18], "branches": []}

import pytest
from pymonet.box import Box

def test_box_init():
    value = 10
    box = Box(value)
    assert box.value == value
