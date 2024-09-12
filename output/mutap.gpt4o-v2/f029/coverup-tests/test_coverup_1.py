# file: f029/__init__.py:4-6
# asked: {"lines": [4, 6], "branches": []}
# gained: {"lines": [4, 6], "branches": []}

import pytest
from f029 import filter_by_prefix

def test_filter_by_prefix():
    # Test with a list of strings where some strings match the prefix
    strings = ["apple", "banana", "apricot", "cherry"]
    prefix = "ap"
    expected = ["apple", "apricot"]
    result = filter_by_prefix(strings, prefix)
    assert result == expected

    # Test with a list of strings where no strings match the prefix
    strings = ["apple", "banana", "apricot", "cherry"]
    prefix = "xy"
    expected = []
    result = filter_by_prefix(strings, prefix)
    assert result == expected

    # Test with an empty list of strings
    strings = []
    prefix = "ap"
    expected = []
    result = filter_by_prefix(strings, prefix)
    assert result == expected

    # Test with a list of strings where all strings match the prefix
    strings = ["apple", "apricot", "apex"]
    prefix = "ap"
    expected = ["apple", "apricot", "apex"]
    result = filter_by_prefix(strings, prefix)
    assert result == expected

    # Test with a list of strings where the prefix is empty
    strings = ["apple", "banana", "apricot", "cherry"]
    prefix = ""
    expected = ["apple", "banana", "apricot", "cherry"]
    result = filter_by_prefix(strings, prefix)
    assert result == expected
