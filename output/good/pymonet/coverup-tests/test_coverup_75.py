# file pymonet/box.py:13-18
# lines [13, 18]
# branches []

import pytest
from pymonet.box import Box

def test_box_initialization():
    # Test initialization of Box with an integer
    int_box = Box(123)
    assert int_box.value == 123

    # Test initialization of Box with a string
    str_box = Box("test")
    assert str_box.value == "test"

    # Test initialization of Box with a list
    list_box = Box([1, 2, 3])
    assert list_box.value == [1, 2, 3]

    # Test initialization of Box with a dictionary
    dict_box = Box({'a': 1, 'b': 2})
    assert dict_box.value == {'a': 1, 'b': 2}

    # Test initialization of Box with None
    none_box = Box(None)
    assert none_box.value is None
