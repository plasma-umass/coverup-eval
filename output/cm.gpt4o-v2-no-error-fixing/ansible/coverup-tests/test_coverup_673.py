# file: lib/ansible/module_utils/urls.py:1478-1487
# asked: {"lines": [1478, 1487], "branches": []}
# gained: {"lines": [1478, 1487], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.urls import Request

@pytest.fixture
def mock_open():
    with patch.object(Request, 'open', return_value=MagicMock()) as mock_method:
        yield mock_method

def test_post_method_executes_open(mock_open):
    req = Request()
    url = "http://example.com"
    data = b"test data"
    headers = {"Content-Type": "application/json"}

    response = req.post(url, data=data, headers=headers)

    mock_open.assert_called_once_with('POST', url, data=data, headers=headers)
    assert response == mock_open.return_value
