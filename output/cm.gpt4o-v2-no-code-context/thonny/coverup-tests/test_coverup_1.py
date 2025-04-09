# file: thonny/roughparse.py:948-951
# asked: {"lines": [948, 951], "branches": []}
# gained: {"lines": [948, 951], "branches": []}

import pytest
from thonny.roughparse import _is_char_in_string

def test_is_char_in_string():
    # Call the function to ensure the lines are executed
    result = _is_char_in_string(0)
    
    # Verify the postcondition
    assert result == 1
