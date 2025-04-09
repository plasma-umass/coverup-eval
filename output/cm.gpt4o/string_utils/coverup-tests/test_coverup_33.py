# file string_utils/validation.py:159-172
# lines [159, 172]
# branches []

import pytest
from string_utils.validation import is_decimal

def test_is_decimal():
    # Test cases where the function should return True
    assert is_decimal('42.0') == True
    assert is_decimal('-42.0') == True

    # Test cases where the function should return False
    assert is_decimal('42') == False
    assert is_decimal('-42') == False
    assert is_decimal('4e1') == False
    assert is_decimal('-4e1') == False
    assert is_decimal('abc') == False
    assert is_decimal('') == False

    # Test cases with edge cases
    assert is_decimal('.') == False
    assert is_decimal('-.') == False
    assert is_decimal('0.') == False
    assert is_decimal('.0') == True
