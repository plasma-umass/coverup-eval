# file: lib/ansible/module_utils/urls.py:1511-1519
# asked: {"lines": [1511, 1519], "branches": []}
# gained: {"lines": [1511, 1519], "branches": []}

import pytest
from unittest.mock import patch, MagicMock

# Assuming the Request class is imported from ansible/module_utils/urls.py
from ansible.module_utils.urls import Request

@pytest.fixture
def mock_open(monkeypatch):
    mock_open = MagicMock()
    monkeypatch.setattr(Request, 'open', mock_open)
    return mock_open

def test_request_delete(mock_open):
    request = Request()
    url = 'http://example.com'
    kwargs = {'param1': 'value1'}

    response = request.delete(url, **kwargs)

    mock_open.assert_called_once_with('DELETE', url, **kwargs)
    assert response == mock_open.return_value
