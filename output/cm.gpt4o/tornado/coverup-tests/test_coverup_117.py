# file tornado/escape.py:173-175
# lines [173, 174, 175]
# branches []

import pytest
from tornado.escape import utf8

def test_utf8_bytes():
    # Test the utf8 function with bytes input
    input_value = b"test"
    result = utf8(input_value)
    assert result == input_value

# Ensure to clean up if any setup was done (not needed in this case)
