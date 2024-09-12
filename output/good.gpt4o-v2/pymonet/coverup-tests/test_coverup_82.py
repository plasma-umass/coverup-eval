# file: pymonet/box.py:13-18
# asked: {"lines": [13, 18], "branches": []}
# gained: {"lines": [13, 18], "branches": []}

import pytest
from pymonet.box import Box

def test_box_initialization():
    # Test initialization with an integer
    box_int = Box(10)
    assert box_int.value == 10

    # Test initialization with a string
    box_str = Box("test")
    assert box_str.value == "test"

    # Test initialization with a list
    box_list = Box([1, 2, 3])
    assert box_list.value == [1, 2, 3]

    # Test initialization with a dictionary
    box_dict = Box({"key": "value"})
    assert box_dict.value == {"key": "value"}
