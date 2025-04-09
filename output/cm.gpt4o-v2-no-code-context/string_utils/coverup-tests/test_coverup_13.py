# file: string_utils/validation.py:621-638
# asked: {"lines": [621, 637, 638], "branches": []}
# gained: {"lines": [621, 637, 638], "branches": []}

import pytest
from string_utils.validation import is_isbn_13

def test_is_isbn_13_valid_with_hyphens():
    assert is_isbn_13('978-0312498580') == True

def test_is_isbn_13_valid_without_hyphens():
    assert is_isbn_13('9780312498580') == True

def test_is_isbn_13_invalid_with_hyphens():
    assert is_isbn_13('978-0312498581') == False

def test_is_isbn_13_invalid_without_hyphens():
    assert is_isbn_13('9780312498581') == False

def test_is_isbn_13_normalize_false_valid():
    assert is_isbn_13('9780312498580', normalize=False) == True

def test_is_isbn_13_normalize_false_invalid():
    assert is_isbn_13('978-0312498580', normalize=False) == False
