# file lib/ansible/plugins/filter/urls.py:26-27
# lines [26, 27]
# branches []

import pytest
from ansible.plugins.filter.urls import do_urldecode

def test_do_urldecode(mocker):
    # Mock the unicode_urldecode function
    mock_unicode_urldecode = mocker.patch('ansible.plugins.filter.urls.unicode_urldecode')
    
    # Define a test string
    test_string = "test%20string"
    
    # Define the expected result
    expected_result = "test string"
    
    # Set the mock to return the expected result
    mock_unicode_urldecode.return_value = expected_result
    
    # Call the function under test
    result = do_urldecode(test_string)
    
    # Assert that the mock was called with the correct argument
    mock_unicode_urldecode.assert_called_once_with(test_string)
    
    # Assert that the result is as expected
    assert result == expected_result
