# file: thonny/roughparse.py:948-951
# asked: {"lines": [948, 951], "branches": []}
# gained: {"lines": [948, 951], "branches": []}

import pytest
from thonny.roughparse import _is_char_in_string

def test_is_char_in_string():
    # Test with a sample text index
    text_index = 5
    result = _is_char_in_string(text_index)
    
    # Verify the result is always 1
    assert result == 1
