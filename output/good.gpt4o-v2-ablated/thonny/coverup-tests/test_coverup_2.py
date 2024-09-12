# file: thonny/roughparse.py:948-951
# asked: {"lines": [948, 951], "branches": []}
# gained: {"lines": [948, 951], "branches": []}

import pytest

from thonny.roughparse import _is_char_in_string

def test_is_char_in_string():
    # Test that _is_char_in_string always returns 1
    assert _is_char_in_string(0) == 1
    assert _is_char_in_string(10) == 1
    assert _is_char_in_string(-1) == 1
    assert _is_char_in_string(100) == 1
