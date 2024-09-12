# file: f012/__init__.py:4-12
# asked: {"lines": [4, 6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 0], [10, 11], [11, 10], [11, 12]]}
# gained: {"lines": [4, 6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 11], [11, 10], [11, 12]]}

import pytest
from f012 import longest

def test_longest_empty_list():
    assert longest([]) is None

def test_longest_single_string():
    assert longest(["a"]) == "a"

def test_longest_multiple_strings():
    assert longest(["a", "ab", "abc"]) == "abc"

def test_longest_multiple_strings_same_length():
    assert longest(["abc", "def", "ghi"]) == "abc"

def test_longest_with_mixed_none_and_strings():
    assert longest(["a", "ab", "abc"]) == "abc"
