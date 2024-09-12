# file: f132/__init__.py:1-18
# asked: {"lines": [1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}

import pytest
from f132 import is_nested

def test_is_nested_no_brackets():
    assert not is_nested("no brackets here")

def test_is_nested_single_pair():
    assert not is_nested("[single pair]")

def test_is_nested_nested():
    assert is_nested("[nested [brackets]]")

def test_is_nested_multiple_pairs():
    assert is_nested("[first pair][second pair]")

def test_is_nested_overlapping_pairs():
    assert is_nested("[[overlapping] pairs]")

def test_is_nested_empty_string():
    assert not is_nested("")

def test_is_nested_only_opening():
    assert not is_nested("[[[[")

def test_is_nested_only_closing():
    assert not is_nested("]]]]")

def test_is_nested_mixed_characters():
    assert is_nested("[a[b]c]d[e]f")
