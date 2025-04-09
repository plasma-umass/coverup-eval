# file: string_utils/validation.py:159-172
# asked: {"lines": [172], "branches": []}
# gained: {"lines": [172], "branches": []}

import pytest
from string_utils.validation import is_decimal

def test_is_decimal_with_decimal_string():
    assert is_decimal('42.0') == True

def test_is_decimal_with_integer_string():
    assert is_decimal('42') == False

def test_is_decimal_with_scientific_notation():
    assert is_decimal('1e3') == False

def test_is_decimal_with_negative_decimal():
    assert is_decimal('-9.12') == True

def test_is_decimal_with_invalid_number():
    assert is_decimal('1 2 3') == False
