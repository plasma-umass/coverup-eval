# file string_utils/validation.py:601-618
# lines [601, 617, 618]
# branches []

import pytest
from string_utils.validation import is_isbn_10

def test_is_isbn_10_valid_isbn():
    assert is_isbn_10('1506715214') == True
    assert is_isbn_10('150-6715214') == True

def test_is_isbn_10_invalid_isbn():
    assert is_isbn_10('150671521X') == False
    assert is_isbn_10('150-671521X') == False

def test_is_isbn_10_normalize_false():
    assert is_isbn_10('150-6715214', normalize=False) == False
    assert is_isbn_10('1506715214', normalize=False) == True

def test_is_isbn_10_invalid_length():
    assert is_isbn_10('150671521') == False
    assert is_isbn_10('15067152145') == False

def test_is_isbn_10_invalid_characters():
    assert is_isbn_10('15067152A4') == False
    assert is_isbn_10('150-67152A4') == False
