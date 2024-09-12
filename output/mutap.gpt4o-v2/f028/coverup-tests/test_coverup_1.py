# file: f028/__init__.py:4-6
# asked: {"lines": [4, 6], "branches": []}
# gained: {"lines": [4, 6], "branches": []}

import pytest
from f028 import concatenate

def test_concatenate():
    # Test with a list of strings
    result = concatenate(["hello", " ", "world"])
    assert result == "hello world"

    # Test with an empty list
    result = concatenate([])
    assert result == ""

    # Test with a list of one string
    result = concatenate(["single"])
    assert result == "single"

    # Test with a list of multiple empty strings
    result = concatenate(["", "", ""])
    assert result == ""

    # Test with a list of strings containing special characters
    result = concatenate(["hello", "\n", "world"])
    assert result == "hello\nworld"
