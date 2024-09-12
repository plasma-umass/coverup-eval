# file: thonny/roughparse.py:954-965
# asked: {"lines": [962, 963, 965], "branches": []}
# gained: {"lines": [962, 963, 965], "branches": []}

import pytest

# Mock function to simulate _is_char_in_string behavior
def mock_is_char_in_string(index):
    # Simulate that characters at even indices are in a string
    return int(index.split('+')[1][:-1]) % 2 == 0

# Import the function to be tested
from thonny.roughparse import _build_char_in_string_func

def test_build_char_in_string_func(monkeypatch):
    # Patch the _is_char_in_string function with our mock
    monkeypatch.setattr('thonny.roughparse._is_char_in_string', mock_is_char_in_string)
    
    # Create the function with a start index
    startindex = "1.0"
    char_in_string_func = _build_char_in_string_func(startindex)
    
    # Test the function with different offsets
    assert char_in_string_func(0) == True  # 1.0 + 0c -> 1.0 (even index)
    assert char_in_string_func(1) == False # 1.0 + 1c -> 1.1 (odd index)
    assert char_in_string_func(2) == True  # 1.0 + 2c -> 1.2 (even index)
    assert char_in_string_func(3) == False # 1.0 + 3c -> 1.3 (odd index)
