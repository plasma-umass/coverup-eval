# file string_utils/validation.py:83-95
# lines [83, 95]
# branches []

import pytest
from string_utils.validation import is_string

def test_is_string():
    # Test with a string
    assert is_string('foo') == True
    
    # Test with a bytes object
    assert is_string(b'foo') == False
    
    # Test with an integer
    assert is_string(123) == False
    
    # Test with a list
    assert is_string(['foo']) == False
    
    # Test with None
    assert is_string(None) == False
    
    # Test with a float
    assert is_string(3.14) == False
    
    # Test with a boolean
    assert is_string(True) == False
