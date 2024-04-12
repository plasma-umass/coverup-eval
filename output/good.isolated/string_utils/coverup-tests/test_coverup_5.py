# file string_utils/validation.py:98-113
# lines [98, 113]
# branches []

import pytest
from string_utils.validation import is_full_string

def test_is_full_string():
    assert not is_full_string(None), "None should return False"
    assert not is_full_string(''), "Empty string should return False"
    assert not is_full_string(' '), "String with only spaces should return False"
    assert is_full_string('hello'), "Non-empty string should return True"
    assert is_full_string(' hello '), "String with non-space characters should return True"
