# file string_utils/validation.py:621-638
# lines [621, 637, 638]
# branches []

import pytest
from string_utils.validation import is_isbn_13

def test_is_isbn_13_valid_isbn():
    assert is_isbn_13('9780312498580') == True
    assert is_isbn_13('978-0312498580') == True

def test_is_isbn_13_invalid_isbn():
    assert is_isbn_13('9780312498581') == False
    assert is_isbn_13('978-0312498581') == False

def test_is_isbn_13_normalize_false():
    assert is_isbn_13('978-0312498580', normalize=False) == False
    assert is_isbn_13('9780312498580', normalize=False) == True

def test_is_isbn_13_invalid_format():
    assert is_isbn_13('978031249858') == False
    assert is_isbn_13('978-031249858') == False
    assert is_isbn_13('97803124985800') == False
    assert is_isbn_13('978-03124985800') == False
    assert is_isbn_13('978031249858a') == False
    assert is_isbn_13('978-031249858a') == False
