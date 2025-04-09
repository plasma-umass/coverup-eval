# file thonny/roughparse.py:954-965
# lines [954, 962, 963, 965]
# branches []

import pytest
from thonny.roughparse import _build_char_in_string_func

def test_build_char_in_string_func(mocker):
    # Mock the _is_char_in_string function
    mock_is_char_in_string = mocker.patch('thonny.roughparse._is_char_in_string', return_value=True)
    
    # Define a start index
    startindex = "1.0"
    
    # Build the function
    char_in_string_func = _build_char_in_string_func(startindex)
    
    # Test the inner function with an offset
    offset = 5
    result = char_in_string_func(offset)
    
    # Verify the mock was called with the correct parameters
    mock_is_char_in_string.assert_called_once_with("1.0+5c")
    
    # Assert the result is as expected
    assert result == True
