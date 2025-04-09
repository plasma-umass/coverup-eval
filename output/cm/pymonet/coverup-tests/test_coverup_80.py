# file pymonet/utils.py:25-34
# lines [25, 34]
# branches []

import pytest
from pymonet.utils import identity

def test_identity():
    # Test with an integer
    assert identity(1) == 1
    # Test with a string
    assert identity("test") == "test"
    # Test with a list
    assert identity([1, 2, 3]) == [1, 2, 3]
    # Test with a dictionary
    assert identity({"key": "value"}) == {"key": "value"}
    # Test with None
    assert identity(None) is None
