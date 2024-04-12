# file tornado/escape.py:204-206
# lines [204, 205, 206]
# branches []

import pytest
from tornado.escape import to_unicode

def test_to_unicode_with_str():
    # Test the to_unicode function with a string input
    input_str = "test string"
    result = to_unicode(input_str)
    assert result == input_str, "The to_unicode function should return the original string when given a string input"
