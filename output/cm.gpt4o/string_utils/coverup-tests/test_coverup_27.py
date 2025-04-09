# file string_utils/manipulation.py:598-608
# lines [598, 608]
# branches []

import pytest
from string_utils.manipulation import decompress

def test_decompress(mocker):
    # Mock the __StringCompressor.decompress method
    mock_decompress = mocker.patch('string_utils.manipulation.__StringCompressor.decompress')
    
    # Define the input and expected output
    input_string = "compressed_string"
    encoding = "utf-8"
    expected_output = "original_string"
    
    # Set the return value of the mock
    mock_decompress.return_value = expected_output
    
    # Call the decompress function
    result = decompress(input_string, encoding)
    
    # Assert that the mock was called with the correct arguments
    mock_decompress.assert_called_once_with(input_string, encoding)
    
    # Assert that the result is as expected
    assert result == expected_output
