# file string_utils/validation.py:83-95
# lines [83, 95]
# branches []

import pytest
from string_utils.validation import is_string

def test_is_string_with_string():
    assert is_string('foo') == True, "Should return True for string input"

def test_is_string_with_bytes():
    assert is_string(b'foo') == False, "Should return False for bytes input"

def test_is_string_with_non_string():
    assert is_string(123) == False, "Should return False for non-string input"
