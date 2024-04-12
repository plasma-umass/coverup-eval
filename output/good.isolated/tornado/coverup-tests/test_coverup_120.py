# file tornado/escape.py:173-175
# lines [173, 174, 175]
# branches []

import pytest
from tornado.escape import utf8

def test_utf8_with_bytes_input():
    # Test the utf8 function with bytes input to cover the overload
    input_bytes = b"test bytes"
    result = utf8(input_bytes)
    assert result == input_bytes, "The utf8 function should return the original bytes when given a bytes input"
