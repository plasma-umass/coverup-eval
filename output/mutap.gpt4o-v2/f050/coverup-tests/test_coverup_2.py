# file: f050/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f050 import encode_shift

def test_encode_shift():
    # Test with a simple string
    result = encode_shift("abc")
    assert result == "fgh", f"Expected 'fgh', but got {result}"

    # Test with wrapping around the alphabet
    result = encode_shift("xyz")
    assert result == "cde", f"Expected 'cde', but got {result}"

    # Test with an empty string
    result = encode_shift("")
    assert result == "", f"Expected '', but got {result}"

    # Test with a string containing all letters
    result = encode_shift("abcdefghijklmnopqrstuvwxyz")
    assert result == "fghijklmnopqrstuvwxyzabcde", f"Expected 'fghijklmnopqrstuvwxyzabcde', but got {result}"

    # Test with a string containing repeated letters
    result = encode_shift("aaa")
    assert result == "fff", f"Expected 'fff', but got {result}"
