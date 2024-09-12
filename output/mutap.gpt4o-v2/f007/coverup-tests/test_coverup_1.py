# file: f007/__init__.py:4-6
# asked: {"lines": [4, 6], "branches": []}
# gained: {"lines": [4, 6], "branches": []}

import pytest
from f007 import filter_by_substring

def test_filter_by_substring():
    # Test case where the substring is present in some strings
    strings = ["apple", "banana", "apricot", "cherry"]
    substring = "ap"
    expected = ["apple", "apricot"]
    result = filter_by_substring(strings, substring)
    assert result == expected

    # Test case where the substring is not present in any string
    strings = ["apple", "banana", "apricot", "cherry"]
    substring = "xyz"
    expected = []
    result = filter_by_substring(strings, substring)
    assert result == expected

    # Test case where the substring is an empty string
    strings = ["apple", "banana", "apricot", "cherry"]
    substring = ""
    expected = ["apple", "banana", "apricot", "cherry"]
    result = filter_by_substring(strings, substring)
    assert result == expected

    # Test case where the list of strings is empty
    strings = []
    substring = "ap"
    expected = []
    result = filter_by_substring(strings, substring)
    assert result == expected
