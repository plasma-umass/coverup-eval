# file: string_utils/validation.py:601-618
# asked: {"lines": [601, 617, 618], "branches": []}
# gained: {"lines": [601, 617, 618], "branches": []}

import pytest
from string_utils.validation import is_isbn_10

def test_is_isbn_10_valid_isbn():
    assert is_isbn_10('1506715214') == True

def test_is_isbn_10_valid_isbn_with_hyphens():
    assert is_isbn_10('150-6715214') == True

def test_is_isbn_10_invalid_isbn_with_hyphens_no_normalize():
    assert is_isbn_10('150-6715214', normalize=False) == False

def test_is_isbn_10_invalid_isbn():
    assert is_isbn_10('1234567890') == False

def test_is_isbn_10_invalid_isbn_with_hyphens():
    assert is_isbn_10('123-4567890') == False

def test_is_isbn_10_invalid_isbn_with_hyphens_no_normalize():
    assert is_isbn_10('123-4567890', normalize=False) == False

def test_is_isbn_10_empty_string():
    assert is_isbn_10('') == False

def test_is_isbn_10_invalid_characters():
    assert is_isbn_10('15067X5214') == False

def test_is_isbn_10_invalid_length():
    assert is_isbn_10('150671521') == False
    assert is_isbn_10('15067152145') == False
