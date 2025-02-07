# file: lib/ansible/module_utils/urls.py:1448-1456
# asked: {"lines": [1448, 1456], "branches": []}
# gained: {"lines": [1448, 1456], "branches": []}

import pytest
from ansible.module_utils.urls import Request
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_open():
    with patch.object(Request, 'open', return_value='mocked_response') as mock_method:
        yield mock_method

def test_request_get_executes_open(mock_open):
    req = Request()
    url = 'http://example.com'
    response = req.get(url)
    
    mock_open.assert_called_once_with('GET', url)
    assert response == 'mocked_response'
