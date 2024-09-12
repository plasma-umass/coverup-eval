# file: string_utils/validation.py:141-156
# asked: {"lines": [141, 156], "branches": []}
# gained: {"lines": [141, 156], "branches": []}

import pytest
from string_utils.validation import is_integer

def test_is_integer_with_integer_string():
    assert is_integer('42') == True

def test_is_integer_with_float_string():
    assert is_integer('42.0') == False

def test_is_integer_with_negative_integer_string():
    assert is_integer('-42') == True

def test_is_integer_with_scientific_notation():
    assert is_integer('1e5') == True

def test_is_integer_with_non_number_string():
    assert is_integer('abc') == False

def test_is_integer_with_empty_string():
    assert is_integer('') == False

def test_is_integer_with_space_string():
    assert is_integer(' ') == False

def test_is_integer_with_special_characters():
    assert is_integer('@#$') == False

def test_is_integer_with_signed_float_string():
    assert is_integer('-42.0') == False

def test_is_integer_with_positive_sign():
    assert is_integer('+42') == True
