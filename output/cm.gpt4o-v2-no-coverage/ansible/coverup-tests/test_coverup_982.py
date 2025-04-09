# file: lib/ansible/module_utils/urls.py:1458-1466
# asked: {"lines": [1458, 1466], "branches": []}
# gained: {"lines": [1458, 1466], "branches": []}

import pytest
from ansible.module_utils.urls import Request
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_open():
    with patch.object(Request, 'open', return_value=MagicMock()) as mock_method:
        yield mock_method

def test_options_method(mock_open):
    req = Request()
    url = 'http://example.com'
    response = req.options(url, headers={'Custom-Header': 'value'})

    # Assert that the open method was called with the correct parameters
    mock_open.assert_called_once_with('OPTIONS', url, headers={'Custom-Header': 'value'})
    
    # Assert that the response is the mock object returned by open
    assert response == mock_open.return_value
