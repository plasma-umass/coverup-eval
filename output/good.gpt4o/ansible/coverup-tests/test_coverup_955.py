# file lib/ansible/module_utils/urls.py:1448-1456
# lines [1448, 1456]
# branches []

import pytest
from unittest.mock import patch, MagicMock

# Assuming the Request class is imported from ansible.module_utils.urls
from ansible.module_utils.urls import Request

@pytest.fixture
def mock_open(mocker):
    return mocker.patch('ansible.module_utils.urls.Request.open', return_value=MagicMock(spec=['name']))

def test_request_get(mock_open):
    request = Request()
    url = 'http://example.com'
    response = request.get(url, headers={'User-Agent': 'pytest'})

    # Verify that the open method was called with the correct parameters
    mock_open.assert_called_once_with('GET', url, headers={'User-Agent': 'pytest'})

    # Verify that the response is an instance of the mocked HTTPResponse
    assert isinstance(response, MagicMock)
