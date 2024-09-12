# file: lib/ansible/module_utils/urls.py:1478-1487
# asked: {"lines": [1478, 1487], "branches": []}
# gained: {"lines": [1478, 1487], "branches": []}

import pytest
from unittest.mock import Mock, patch

# Assuming the Request class is in a module named ansible.module_utils.urls
from ansible.module_utils.urls import Request

@pytest.fixture
def mock_open():
    with patch('ansible.module_utils.urls.Request.open') as mock_open:
        yield mock_open

def test_post_with_data(mock_open):
    request = Request()
    url = 'http://example.com'
    data = b'some data'
    mock_response = Mock()
    mock_open.return_value = mock_response

    response = request.post(url, data=data)

    mock_open.assert_called_once_with('POST', url, data=data)
    assert response == mock_response

def test_post_without_data(mock_open):
    request = Request()
    url = 'http://example.com'
    mock_response = Mock()
    mock_open.return_value = mock_response

    response = request.post(url)

    mock_open.assert_called_once_with('POST', url, data=None)
    assert response == mock_response

def test_post_with_kwargs(mock_open):
    request = Request()
    url = 'http://example.com'
    data = b'some data'
    headers = {'Content-Type': 'application/json'}
    mock_response = Mock()
    mock_open.return_value = mock_response

    response = request.post(url, data=data, headers=headers)

    mock_open.assert_called_once_with('POST', url, data=data, headers=headers)
    assert response == mock_response
