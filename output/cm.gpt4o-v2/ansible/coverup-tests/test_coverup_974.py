# file: lib/ansible/module_utils/urls.py:1500-1509
# asked: {"lines": [1500, 1509], "branches": []}
# gained: {"lines": [1500, 1509], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.urls import Request

@pytest.fixture
def request_instance():
    return Request()

def test_patch_method(request_instance):
    url = "http://example.com"
    data = b"test data"
    response_mock = MagicMock()

    with patch.object(request_instance, 'open', return_value=response_mock) as mock_open:
        response = request_instance.patch(url, data=data)
        mock_open.assert_called_once_with('PATCH', url, data=data)
        assert response == response_mock
