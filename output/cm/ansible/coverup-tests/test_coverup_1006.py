# file lib/ansible/module_utils/urls.py:1478-1487
# lines [1478, 1487]
# branches []

import pytest
from ansible.module_utils.urls import Request
from unittest.mock import MagicMock

# Define a test function to cover the post method
def test_request_post(mocker):
    # Mock the open method
    mocker.patch.object(Request, 'open', return_value='HTTPResponse')

    # Create an instance of the Request class
    request = Request()

    # Call the post method
    response = request.post('http://example.com', data=b'test_data')

    # Assert that the open method was called with the correct parameters
    Request.open.assert_called_once_with('POST', 'http://example.com', data=b'test_data')

    # Assert that the response is as expected
    assert response == 'HTTPResponse'

# Clean up after the test
@pytest.fixture(autouse=True)
def clean_up(mocker):
    yield
    mocker.stopall()
