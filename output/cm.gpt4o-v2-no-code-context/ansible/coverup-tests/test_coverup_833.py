# file: lib/ansible/module_utils/urls.py:1478-1487
# asked: {"lines": [1478, 1487], "branches": []}
# gained: {"lines": [1478, 1487], "branches": []}

import pytest
from unittest.mock import Mock, patch

# Assuming the Request class is imported from ansible/module_utils/urls.py
from ansible.module_utils.urls import Request

@pytest.fixture
def mock_open():
    with patch('ansible.module_utils.urls.Request.open') as mock_open:
        yield mock_open

def test_post_method(mock_open):
    request = Request()
    url = 'http://example.com'
    data = b'some data'
    response = Mock()
    mock_open.return_value = response

    result = request.post(url, data=data)

    mock_open.assert_called_once_with('POST', url, data=data)
    assert result == response
