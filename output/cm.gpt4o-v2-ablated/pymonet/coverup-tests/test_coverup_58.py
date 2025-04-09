# file: pymonet/box.py:26-35
# asked: {"lines": [26, 35], "branches": []}
# gained: {"lines": [26, 35], "branches": []}

import pytest
from pymonet.box import Box

def test_box_map():
    # Test case 1: Mapping an integer value
    box = Box(5)
    new_box = box.map(lambda x: x * 2)
    assert new_box.value == 10

    # Test case 2: Mapping a string value
    box = Box("hello")
    new_box = box.map(lambda x: x.upper())
    assert new_box.value == "HELLO"

    # Test case 3: Mapping a list
    box = Box([1, 2, 3])
    new_box = box.map(lambda x: [i * 2 for i in x])
    assert new_box.value == [2, 4, 6]

    # Test case 4: Mapping with a function that returns a different type
    box = Box(3.14)
    new_box = box.map(lambda x: str(x))
    assert new_box.value == "3.14"

    # Test case 5: Mapping with a function that raises an exception
    box = Box(10)
    with pytest.raises(ZeroDivisionError):
        box.map(lambda x: x / 0)
