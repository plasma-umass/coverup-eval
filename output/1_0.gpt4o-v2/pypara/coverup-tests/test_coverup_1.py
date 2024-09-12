# file: pypara/commons/others.py:27-34
# asked: {"lines": [27, 34], "branches": []}
# gained: {"lines": [27, 34], "branches": []}

import pytest
from pypara.commons.others import identity

def test_identity():
    # Test with an integer
    assert identity(5) == 5

    # Test with a string
    assert identity("test") == "test"

    # Test with a list
    assert identity([1, 2, 3]) == [1, 2, 3]

    # Test with a dictionary
    assert identity({"key": "value"}) == {"key": "value"}

    # Test with a custom object
    class CustomObject:
        def __init__(self, value):
            self.value = value

    obj = CustomObject(10)
    assert identity(obj) is obj
