# file: string_utils/validation.py:516-529
# asked: {"lines": [516, 529], "branches": []}
# gained: {"lines": [516, 529], "branches": []}

import pytest
from string_utils.validation import is_isogram

def test_is_isogram_true():
    assert is_isogram('dermatoglyphics') == True

def test_is_isogram_false():
    assert is_isogram('hello') == False

def test_is_isogram_empty_string():
    assert is_isogram('') == False

def test_is_isogram_non_string_input():
    assert is_isogram(None) == False
    assert is_isogram(12345) == False
    assert is_isogram(['a', 'b', 'c']) == False

def test_is_isogram_single_character():
    assert is_isogram('a') == True

def test_is_isogram_special_characters():
    assert is_isogram('!@#$%^&*()') == True

def test_is_isogram_mixed_case():
    assert is_isogram('Dermatoglyphics') == True
