# file: lib/ansible/module_utils/urls.py:1448-1456
# asked: {"lines": [1448, 1456], "branches": []}
# gained: {"lines": [1448, 1456], "branches": []}

import pytest
from unittest.mock import patch, MagicMock

# Assuming the Request class is part of a module named 'urls'
from ansible.module_utils.urls import Request

@pytest.fixture
def mock_open(monkeypatch):
    mock_open = MagicMock()
    monkeypatch.setattr(Request, 'open', mock_open)
    return mock_open

def test_request_get(mock_open):
    request = Request()
    url = 'http://example.com'
    kwargs = {'param1': 'value1'}

    # Call the get method
    response = request.get(url, **kwargs)

    # Assert that the open method was called with the correct parameters
    mock_open.assert_called_once_with('GET', url, **kwargs)

    # Assert that the response is the return value of the open method
    assert response == mock_open.return_value
