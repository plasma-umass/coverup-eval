# file: lib/ansible/module_utils/urls.py:1468-1476
# asked: {"lines": [1468, 1476], "branches": []}
# gained: {"lines": [1468, 1476], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.urls import Request

@pytest.fixture
def mock_open():
    with patch.object(Request, 'open', return_value=MagicMock()) as mock_method:
        yield mock_method

def test_head_method(mock_open):
    req = Request()
    url = "http://example.com"
    headers = {"Custom-Header": "value"}
    
    response = req.head(url, headers=headers)
    
    mock_open.assert_called_once_with('HEAD', url, headers=headers)
    assert response == mock_open.return_value
