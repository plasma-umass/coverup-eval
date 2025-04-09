# file string_utils/manipulation.py:405-430
# lines [429, 430]
# branches []

import pytest
from string_utils.manipulation import prettify

def test_prettify_executes_missing_lines(mocker):
    # Mock the __StringFormatter class and its format method
    mock_formatter = mocker.patch('string_utils.manipulation.__StringFormatter')
    mock_formatter_instance = mock_formatter.return_value
    mock_formatter_instance.format.return_value = 'Mocked formatted string'
    
    # Call the prettify function which should use the mocked __StringFormatter
    result = prettify('Some input string')
    
    # Assert that the format method was called
    mock_formatter_instance.format.assert_called_once()
    
    # Assert that the result is what the mocked format method returns
    assert result == 'Mocked formatted string'
