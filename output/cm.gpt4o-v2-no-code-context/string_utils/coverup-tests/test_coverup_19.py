# file: string_utils/validation.py:601-618
# asked: {"lines": [601, 617, 618], "branches": []}
# gained: {"lines": [601, 617, 618], "branches": []}

import pytest
from string_utils.validation import is_isbn_10

def test_is_isbn_10_valid_with_hyphens():
    assert is_isbn_10('150-6715214') == True

def test_is_isbn_10_valid_without_hyphens():
    assert is_isbn_10('1506715214') == True

def test_is_isbn_10_invalid_with_hyphens_normalize_false():
    assert is_isbn_10('150-6715214', normalize=False) == False

def test_is_isbn_10_invalid_length():
    assert is_isbn_10('150671521') == False

def test_is_isbn_10_invalid_characters():
    assert is_isbn_10('15067152X4') == False

def test_is_isbn_10_empty_string():
    assert is_isbn_10('') == False

def test_is_isbn_10_invalid_with_hyphens():
    assert is_isbn_10('150-67152X4') == False
