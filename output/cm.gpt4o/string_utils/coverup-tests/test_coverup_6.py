# file string_utils/validation.py:98-113
# lines [98, 113]
# branches []

import pytest
from string_utils.validation import is_full_string

def test_is_full_string():
    # Test with None
    assert not is_full_string(None), "Expected False for None input"
    
    # Test with empty string
    assert not is_full_string(''), "Expected False for empty string"
    
    # Test with string containing only spaces
    assert not is_full_string(' '), "Expected False for string with only spaces"
    
    # Test with non-empty string
    assert is_full_string('hello'), "Expected True for non-empty string"
    
    # Test with string containing spaces and characters
    assert is_full_string(' hello '), "Expected True for string with spaces and characters"
    
    # Test with non-string input
    assert not is_full_string(123), "Expected False for non-string input"
