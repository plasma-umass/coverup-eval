# file: lib/ansible/module_utils/urls.py:1489-1498
# asked: {"lines": [1489, 1498], "branches": []}
# gained: {"lines": [1489, 1498], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.urls import Request

@pytest.fixture
def mock_open():
    with patch.object(Request, 'open', return_value=MagicMock()) as mock_method:
        yield mock_method

def test_put_method(mock_open):
    req = Request()
    url = "http://example.com"
    data = b"test data"
    headers = {"Content-Type": "application/json"}

    response = req.put(url, data=data, headers=headers)

    mock_open.assert_called_once_with('PUT', url, data=data, headers=headers)
    assert response == mock_open.return_value
