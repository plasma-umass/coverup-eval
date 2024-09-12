# file: f011/__init__.py:4-12
# asked: {"lines": [4, 6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}
# gained: {"lines": [4, 6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}

import pytest
from f011 import string_xor

def test_string_xor_equal_length():
    assert string_xor("1010", "1010") == "0000"
    assert string_xor("1111", "0000") == "1111"

def test_string_xor_different_length():
    assert string_xor("101", "1010") == "000"
    assert string_xor("111", "0000") == "111"

def test_string_xor_empty_strings():
    assert string_xor("", "") == ""

def test_string_xor_single_characters():
    assert string_xor("1", "1") == "0"
    assert string_xor("0", "1") == "1"
