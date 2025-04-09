# file: string_utils/validation.py:159-172
# asked: {"lines": [159, 172], "branches": []}
# gained: {"lines": [159, 172], "branches": []}

import pytest
from string_utils.validation import is_decimal
from string_utils.errors import InvalidInputError

def test_is_decimal_with_decimal_string():
    assert is_decimal('42.0') == True

def test_is_decimal_with_integer_string():
    assert is_decimal('42') == False

def test_is_decimal_with_scientific_notation():
    assert is_decimal('1e3') == False

def test_is_decimal_with_invalid_string():
    assert is_decimal('abc') == False

def test_is_decimal_with_empty_string():
    assert is_decimal('') == False

def test_is_decimal_with_non_string_input():
    with pytest.raises(InvalidInputError):
        is_decimal(42)
