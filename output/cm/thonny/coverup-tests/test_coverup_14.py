# file thonny/roughparse.py:954-965
# lines [954, 962, 963, 965]
# branches []

import pytest
from thonny.roughparse import _build_char_in_string_func

def test_build_char_in_string_func(mocker):
    # Mock the _is_char_in_string function
    mock_is_char_in_string = mocker.Mock(return_value=True)
    
    # Create the function with a mocked startindex and the mocked _is_char_in_string
    char_in_string_func = _build_char_in_string_func("1.0")
    
    # Replace the _is_char_in_string with the mock
    char_in_string_func.__defaults__ = ("1.0", mock_is_char_in_string)
    
    # Call the function with an offset
    result = char_in_string_func(5)
    
    # Assert that the mock was called with the correct argument
    mock_is_char_in_string.assert_called_once_with("1.0+5c")
    
    # Assert that the result is what the mock returned
    assert result == True
