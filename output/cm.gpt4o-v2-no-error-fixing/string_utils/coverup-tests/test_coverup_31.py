# file: string_utils/validation.py:286-305
# asked: {"lines": [286, 305], "branches": []}
# gained: {"lines": [286, 305], "branches": []}

import pytest
from string_utils.validation import is_camel_case

def test_is_camel_case_with_camel_case_string():
    assert is_camel_case('MyString') == True

def test_is_camel_case_with_lowercase_string():
    assert is_camel_case('mystring') == False

def test_is_camel_case_with_uppercase_string():
    assert is_camel_case('MYSTRING') == False

def test_is_camel_case_with_mixed_case_string():
    assert is_camel_case('myString') == True

def test_is_camel_case_with_number_at_start():
    assert is_camel_case('1MyString') == False

def test_is_camel_case_with_number_in_middle():
    assert is_camel_case('My1String') == True

def test_is_camel_case_with_empty_string():
    assert is_camel_case('') == False

def test_is_camel_case_with_none():
    assert is_camel_case(None) == False

def test_is_camel_case_with_spaces():
    assert is_camel_case(' ') == False

def test_is_camel_case_with_special_characters():
    assert is_camel_case('My@String') == False
