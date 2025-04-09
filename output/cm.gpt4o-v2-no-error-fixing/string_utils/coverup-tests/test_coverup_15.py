# file: string_utils/validation.py:516-529
# asked: {"lines": [516, 529], "branches": []}
# gained: {"lines": [516, 529], "branches": []}

import pytest
from string_utils.validation import is_isogram

def test_is_isogram_with_isogram():
    assert is_isogram('dermatoglyphics') == True

def test_is_isogram_with_non_isogram():
    assert is_isogram('hello') == False

def test_is_isogram_with_empty_string():
    assert is_isogram('') == False

def test_is_isogram_with_none():
    assert is_isogram(None) == False

def test_is_isogram_with_spaces():
    assert is_isogram(' ') == False

def test_is_isogram_with_mixed_characters():
    assert is_isogram('abcABC') == True

def test_is_isogram_with_repeated_characters():
    assert is_isogram('abcabc') == False
