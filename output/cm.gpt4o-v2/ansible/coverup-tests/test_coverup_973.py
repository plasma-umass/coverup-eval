# file: lib/ansible/module_utils/urls.py:1478-1487
# asked: {"lines": [1478, 1487], "branches": []}
# gained: {"lines": [1478, 1487], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.urls import Request

@pytest.fixture
def request_instance():
    return Request()

def test_post_method(request_instance):
    url = "http://example.com"
    data = b"test data"
    mock_response = MagicMock()

    with patch.object(request_instance, 'open', return_value=mock_response) as mock_open:
        response = request_instance.post(url, data=data)
        mock_open.assert_called_once_with('POST', url, data=data)
        assert response == mock_response
