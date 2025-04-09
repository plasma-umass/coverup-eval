# file tornado/escape.py:209-211
# lines [209, 210, 211]
# branches []

import pytest
from tornado.escape import to_unicode

def test_to_unicode_with_bytes():
    # Test the to_unicode function with bytes input
    byte_input = b'This is a test'
    expected_output = 'This is a test'
    
    # Call the function and assert the result is as expected
    result = to_unicode(byte_input)
    assert result == expected_output, "to_unicode did not convert bytes to str correctly"
