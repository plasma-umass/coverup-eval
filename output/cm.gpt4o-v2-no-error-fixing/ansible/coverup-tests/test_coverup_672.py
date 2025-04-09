# file: lib/ansible/module_utils/urls.py:1458-1466
# asked: {"lines": [1458, 1466], "branches": []}
# gained: {"lines": [1458, 1466], "branches": []}

import pytest
from ansible.module_utils.urls import Request
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_open():
    with patch('ansible.module_utils.urls.Request.open') as mock:
        yield mock

def test_options_request(mock_open):
    req = Request()
    url = 'http://example.com'
    mock_response = MagicMock()
    mock_open.return_value = mock_response

    response = req.options(url)

    mock_open.assert_called_once_with('OPTIONS', url)
    assert response == mock_response
