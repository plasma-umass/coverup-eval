# file: string_utils/validation.py:141-156
# asked: {"lines": [141, 156], "branches": []}
# gained: {"lines": [141, 156], "branches": []}

import pytest
from string_utils.validation import is_integer

def test_is_integer_with_integer_string():
    assert is_integer('42') is True

def test_is_integer_with_float_string():
    assert is_integer('42.0') is False

def test_is_integer_with_negative_integer_string():
    assert is_integer('-42') is True

def test_is_integer_with_scientific_notation_integer():
    assert is_integer('1e3') is True

def test_is_integer_with_non_numeric_string():
    assert is_integer('abc') is False

def test_is_integer_with_empty_string():
    assert is_integer('') is False

def test_is_integer_with_whitespace_string():
    assert is_integer('   ') is False

def test_is_integer_with_signed_zero():
    assert is_integer('-0') is True

def test_is_integer_with_positive_sign():
    assert is_integer('+42') is True

def test_is_integer_with_leading_zeros():
    assert is_integer('0042') is True

@pytest.fixture(autouse=True)
def mock_is_number(monkeypatch):
    def mock_is_number(input_string):
        try:
            float(input_string)
            return True
        except ValueError:
            return False
    monkeypatch.setattr('string_utils.validation.is_number', mock_is_number)
