# file: thonny/roughparse.py:954-965
# asked: {"lines": [954, 962, 963, 965], "branches": []}
# gained: {"lines": [954, 962, 963, 965], "branches": []}

import pytest
from thonny.roughparse import _build_char_in_string_func

def test_build_char_in_string_func():
    # Mock the _is_char_in_string function
    def mock_is_char_in_string(text_index):
        return text_index == "1.0+5c"
    
    # Patch the _is_char_in_string function in the module
    import thonny.roughparse
    thonny.roughparse._is_char_in_string = mock_is_char_in_string
    
    # Create the function with a start index
    func = _build_char_in_string_func("1.0")
    
    # Test the inner function
    assert func(5) == True
    assert func(4) == False

    # Clean up by removing the mock
    del thonny.roughparse._is_char_in_string

