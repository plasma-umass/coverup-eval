# file string_utils/validation.py:621-638
# lines [621, 637, 638]
# branches []

import pytest
from string_utils.validation import is_isbn_13

def test_is_isbn_13():
    # Test with a valid ISBN-13 with hyphens
    assert is_isbn_13('978-0312498580') == True
    # Test with a valid ISBN-13 without hyphens
    assert is_isbn_13('9780312498580') == True
    # Test with a valid ISBN-13 with hyphens but normalization turned off
    assert is_isbn_13('978-0312498580', normalize=False) == False
    # Test with an invalid ISBN-13
    assert is_isbn_13('1234567890123') == False
    # Test with an empty string
    assert is_isbn_13('') == False
    # Test with a string that is too short
    assert is_isbn_13('978') == False
    # Test with a string that is too long
    assert is_isbn_13('9780312498580123') == False
    # Test with a string containing invalid characters
    assert is_isbn_13('97803X2498580') == False
