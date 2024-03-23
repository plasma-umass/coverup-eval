# file thonny/roughparse.py:948-951
# lines [948, 951]
# branches []

import pytest
from thonny.roughparse import _is_char_in_string

def test_is_char_in_string():
    # Since the function always returns 1, we just need to call it and assert the result is 1
    assert _is_char_in_string(0) == 1
