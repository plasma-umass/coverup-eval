# file: lib/ansible/module_utils/urls.py:1468-1476
# asked: {"lines": [1468, 1476], "branches": []}
# gained: {"lines": [1468, 1476], "branches": []}

import pytest
from ansible.module_utils.urls import Request
from unittest.mock import patch

@pytest.fixture
def request_instance():
    return Request()

def test_head_method(request_instance):
    url = 'http://example.com'
    with patch.object(request_instance, 'open', return_value='mocked_response') as mock_open:
        response = request_instance.head(url)
        mock_open.assert_called_once_with('HEAD', url)
        assert response == 'mocked_response'
