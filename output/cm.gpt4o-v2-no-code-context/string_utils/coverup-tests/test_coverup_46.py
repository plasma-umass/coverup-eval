# file: string_utils/validation.py:159-172
# asked: {"lines": [159, 172], "branches": []}
# gained: {"lines": [159, 172], "branches": []}

import pytest
from string_utils.validation import is_decimal

def test_is_decimal_with_decimal():
    assert is_decimal('42.0') == True

def test_is_decimal_with_integer():
    assert is_decimal('42') == False

def test_is_decimal_with_negative_decimal():
    assert is_decimal('-42.0') == True

def test_is_decimal_with_scientific_notation():
    assert is_decimal('4.2e1') == True

def test_is_decimal_with_invalid_string():
    assert is_decimal('abc') == False

def test_is_decimal_with_empty_string():
    assert is_decimal('') == False

def test_is_decimal_with_only_dot():
    assert is_decimal('.') == False

def test_is_decimal_with_dot_at_end():
    assert is_decimal('42.') == False

def test_is_decimal_with_dot_at_start():
    assert is_decimal('.42') == True

def test_is_decimal_with_trailing_dot():
    assert is_decimal('42.0.') == False
