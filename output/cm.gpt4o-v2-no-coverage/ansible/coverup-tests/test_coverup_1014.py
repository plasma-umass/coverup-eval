# file: lib/ansible/module_utils/urls.py:1478-1487
# asked: {"lines": [1478, 1487], "branches": []}
# gained: {"lines": [1478, 1487], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.urls import Request

@pytest.fixture
def mock_open():
    with patch('ansible.module_utils.urls.Request.open') as mock:
        yield mock

def test_post_with_data(mock_open):
    req = Request()
    url = 'http://example.com'
    data = b'some data'
    mock_response = MagicMock()
    mock_open.return_value = mock_response

    response = req.post(url, data=data)

    mock_open.assert_called_once_with('POST', url, data=data)
    assert response == mock_response

def test_post_without_data(mock_open):
    req = Request()
    url = 'http://example.com'
    mock_response = MagicMock()
    mock_open.return_value = mock_response

    response = req.post(url)

    mock_open.assert_called_once_with('POST', url, data=None)
    assert response == mock_response

def test_post_with_kwargs(mock_open):
    req = Request()
    url = 'http://example.com'
    headers = {'Content-Type': 'application/json'}
    mock_response = MagicMock()
    mock_open.return_value = mock_response

    response = req.post(url, headers=headers)

    mock_open.assert_called_once_with('POST', url, data=None, headers=headers)
    assert response == mock_response
