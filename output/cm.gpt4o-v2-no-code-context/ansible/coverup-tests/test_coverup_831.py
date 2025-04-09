# file: lib/ansible/module_utils/urls.py:1468-1476
# asked: {"lines": [1468, 1476], "branches": []}
# gained: {"lines": [1468, 1476], "branches": []}

import pytest
from unittest.mock import patch, MagicMock

# Assuming the Request class is imported from ansible/module_utils/urls.py
from ansible.module_utils.urls import Request

@pytest.fixture
def mock_open(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr(Request, 'open', mock)
    return mock

def test_request_head(mock_open):
    request = Request()
    url = 'http://example.com'
    kwargs = {'headers': {'User-Agent': 'test-agent'}}
    
    response = request.head(url, **kwargs)
    
    mock_open.assert_called_once_with('HEAD', url, **kwargs)
    assert response == mock_open.return_value
