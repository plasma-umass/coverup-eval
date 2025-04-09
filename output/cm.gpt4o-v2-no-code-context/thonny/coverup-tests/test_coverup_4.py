# file: thonny/roughparse.py:954-965
# asked: {"lines": [954, 962, 963, 965], "branches": []}
# gained: {"lines": [954, 962, 963, 965], "branches": []}

import pytest
from thonny.roughparse import _build_char_in_string_func

def test_build_char_in_string_func(monkeypatch):
    # Mock the _is_char_in_string function
    def mock_is_char_in_string(index):
        # Simulate behavior based on index
        if index == "1.0+3c":
            return True
        return False

    monkeypatch.setattr('thonny.roughparse._is_char_in_string', mock_is_char_in_string)

    # Create the function with a start index
    startindex = "1.0"
    char_in_string_func = _build_char_in_string_func(startindex)

    # Test the inner function with an offset
    assert char_in_string_func(3) == True
    assert char_in_string_func(0) == False
