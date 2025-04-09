# file: pymonet/box.py:23-24
# asked: {"lines": [23, 24], "branches": []}
# gained: {"lines": [23, 24], "branches": []}

import pytest
from pymonet.box import Box

def test_box_str():
    class TestBox(Box):
        def __init__(self, value):
            self.value = value

    box = TestBox(42)
    assert str(box) == 'Box[value=42]'
