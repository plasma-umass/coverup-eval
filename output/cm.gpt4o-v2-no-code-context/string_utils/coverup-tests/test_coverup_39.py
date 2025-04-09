# file: string_utils/validation.py:141-156
# asked: {"lines": [141, 156], "branches": []}
# gained: {"lines": [141, 156], "branches": []}

import pytest
from string_utils.validation import is_integer

def test_is_integer_with_integer_string():
    assert is_integer('42') is True

def test_is_integer_with_negative_integer_string():
    assert is_integer('-42') is True

def test_is_integer_with_zero():
    assert is_integer('0') is True

def test_is_integer_with_positive_integer_string():
    assert is_integer('+42') is True

def test_is_integer_with_scientific_notation():
    assert is_integer('1e10') is True

def test_is_integer_with_float_string():
    assert is_integer('42.0') is False

def test_is_integer_with_non_numeric_string():
    assert is_integer('abc') is False

def test_is_integer_with_empty_string():
    assert is_integer('') is False

def test_is_integer_with_whitespace_string():
    assert is_integer('   ') is False

def test_is_integer_with_special_characters():
    assert is_integer('42!') is False

def test_is_integer_with_mixed_characters():
    assert is_integer('42abc') is False
