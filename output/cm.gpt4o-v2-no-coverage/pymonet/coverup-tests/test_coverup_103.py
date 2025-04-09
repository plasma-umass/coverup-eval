# file: pymonet/box.py:26-35
# asked: {"lines": [26, 35], "branches": []}
# gained: {"lines": [26, 35], "branches": []}

import pytest
from pymonet.box import Box

def test_box_map():
    # Test that Box.map correctly applies the mapper function and returns a new Box with the mapped value
    box = Box(5)
    mapped_box = box.map(lambda x: x * 2)
    assert isinstance(mapped_box, Box)
    assert mapped_box.value == 10

    # Test with a different type
    box_str = Box("hello")
    mapped_box_str = box_str.map(lambda x: x.upper())
    assert isinstance(mapped_box_str, Box)
    assert mapped_box_str.value == "HELLO"

    # Test with an empty string
    box_empty_str = Box("")
    mapped_box_empty_str = box_empty_str.map(lambda x: x.upper())
    assert isinstance(mapped_box_empty_str, Box)
    assert mapped_box_empty_str.value == ""

    # Test with a list
    box_list = Box([1, 2, 3])
    mapped_box_list = box_list.map(lambda x: [i * 2 for i in x])
    assert isinstance(mapped_box_list, Box)
    assert mapped_box_list.value == [2, 4, 6]

    # Test with a dictionary
    box_dict = Box({"a": 1, "b": 2})
    mapped_box_dict = box_dict.map(lambda x: {k: v * 2 for k, v in x.items()})
    assert isinstance(mapped_box_dict, Box)
    assert mapped_box_dict.value == {"a": 2, "b": 4}
