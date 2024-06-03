# file tornado/escape.py:209-211
# lines [209, 210, 211]
# branches []

import pytest
from tornado.escape import to_unicode

def test_to_unicode_bytes():
    # Test that to_unicode correctly converts bytes to string
    byte_value = b'hello'
    result = to_unicode(byte_value)
    assert result == 'hello'
    assert isinstance(result, str)
