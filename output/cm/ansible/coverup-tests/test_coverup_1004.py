# file lib/ansible/module_utils/urls.py:1448-1456
# lines [1448, 1456]
# branches []

import pytest
from ansible.module_utils.urls import Request
from unittest.mock import MagicMock

# Define a test function to improve coverage
def test_request_get(mocker):
    # Mock the open method
    mock_open = mocker.patch.object(Request, 'open', return_value='mocked_response')

    # Create an instance of the Request class
    request = Request()

    # Call the get method
    response = request.get('http://example.com')

    # Assert that the open method was called with the correct parameters
    mock_open.assert_called_once_with('GET', 'http://example.com')

    # Assert that the response is as expected
    assert response == 'mocked_response'
