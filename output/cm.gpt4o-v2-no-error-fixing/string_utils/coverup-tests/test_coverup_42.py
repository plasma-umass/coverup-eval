# file: string_utils/validation.py:641-657
# asked: {"lines": [656, 657], "branches": []}
# gained: {"lines": [656, 657], "branches": []}

import pytest
from string_utils.validation import is_isbn

def test_is_isbn_valid_isbn13():
    assert is_isbn('9780312498580') == True

def test_is_isbn_valid_isbn10():
    assert is_isbn('1506715214') == True

def test_is_isbn_invalid_isbn():
    assert is_isbn('1234567890') == False

def test_is_isbn_with_hyphens():
    assert is_isbn('978-0-312-49858-0') == True

def test_is_isbn_invalid_characters():
    assert is_isbn('97803124X580') == False

def test_is_isbn_normalize_false():
    assert is_isbn('978-0-312-49858-0', normalize=False) == False
