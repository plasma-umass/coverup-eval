# file: f158/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f158 import find_max

def test_find_max():
    words = ["apple", "banana", "cherry", "date"]
    result = find_max(words)
    assert result == "cherry"

    words = ["a", "bb", "ccc", "dddd"]
    result = find_max(words)
    assert result == "a"

    words = ["abc", "bca", "cab"]
    result = find_max(words)
    assert result == "abc"

    words = ["a", "b", "c"]
    result = find_max(words)
    assert result == "a"

    words = ["abc", "def", "ghi"]
    result = find_max(words)
    assert result == "abc"

    words = ["abc", "def", "ghi", "a"]
    result = find_max(words)
    assert result == "abc"
