# file lib/ansible/module_utils/urls.py:1468-1476
# lines [1468, 1476]
# branches []

import pytest
from ansible.module_utils.urls import Request
from unittest.mock import MagicMock

# Define a test function to cover the head method
def test_request_head(mocker):
    # Mock the open method in the Request class
    mock_open = mocker.patch.object(Request, 'open', return_value='HTTPResponse')

    # Create an instance of the Request class
    request = Request()

    # Call the head method
    response = request.head('http://example.com')

    # Assert that the open method was called with the correct parameters
    mock_open.assert_called_once_with('HEAD', 'http://example.com')

    # Assert that the response is what the mock open method returned
    assert response == 'HTTPResponse'

    # Clean up the mock
    mocker.stopall()
