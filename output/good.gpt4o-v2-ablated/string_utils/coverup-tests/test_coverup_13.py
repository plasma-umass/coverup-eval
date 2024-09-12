# file: string_utils/validation.py:621-638
# asked: {"lines": [621, 637, 638], "branches": []}
# gained: {"lines": [621, 637, 638], "branches": []}

import pytest
from string_utils.validation import is_isbn_13

def test_is_isbn_13_valid_isbn():
    assert is_isbn_13('9780312498580') == True

def test_is_isbn_13_valid_isbn_with_hyphens():
    assert is_isbn_13('978-0312498580') == True

def test_is_isbn_13_invalid_isbn_with_hyphens_normalize_false():
    assert is_isbn_13('978-0312498580', normalize=False) == False

def test_is_isbn_13_invalid_isbn():
    assert is_isbn_13('9780312498581') == False

def test_is_isbn_13_invalid_isbn_with_hyphens():
    assert is_isbn_13('978-0312498581') == False

def test_is_isbn_13_invalid_isbn_with_hyphens_normalize_false():
    assert is_isbn_13('978-0312498581', normalize=False) == False

def test_is_isbn_13_invalid_length():
    assert is_isbn_13('978031249858') == False

def test_is_isbn_13_invalid_characters():
    assert is_isbn_13('97803124985X') == False
