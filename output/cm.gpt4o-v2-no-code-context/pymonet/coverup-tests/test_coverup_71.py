# file: pymonet/box.py:13-18
# asked: {"lines": [13, 18], "branches": []}
# gained: {"lines": [13, 18], "branches": []}

import pytest
from pymonet.box import Box

def test_box_initialization():
    value = 42
    box = Box(value)
    assert box.value == value

def test_box_initialization_with_string():
    value = "test"
    box = Box(value)
    assert box.value == value

def test_box_initialization_with_list():
    value = [1, 2, 3]
    box = Box(value)
    assert box.value == value

def test_box_initialization_with_dict():
    value = {"key": "value"}
    box = Box(value)
    assert box.value == value
