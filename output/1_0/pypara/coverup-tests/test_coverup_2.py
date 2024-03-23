# file pypara/commons/others.py:27-34
# lines [27, 34]
# branches []

import pytest
from pypara.commons.others import identity

def test_identity_function():
    # Test with an integer
    assert identity(5) == 5
    # Test with a string
    assert identity("test") == "test"
    # Test with a list
    assert identity([1, 2, 3]) == [1, 2, 3]
    # Test with a dictionary
    assert identity({"key": "value"}) == {"key": "value"}
