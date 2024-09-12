# file: f050/__init__.py:6-8
# asked: {"lines": [6, 8], "branches": []}
# gained: {"lines": [6, 8], "branches": []}

import pytest
from f050 import decode_shift

def test_decode_shift():
    # Test with a simple string
    result = decode_shift("fghij")
    assert result == "abcde"

    # Test with wrap-around characters
    result = decode_shift("abcde")
    assert result == "vwxyz"

    # Test with an empty string
    result = decode_shift("")
    assert result == ""

    # Test with a string containing all alphabet characters
    result = decode_shift("abcdefghijklmnopqrstuvwxyz")
    assert result == "vwxyzabcdefghijklmnopqrstu"
