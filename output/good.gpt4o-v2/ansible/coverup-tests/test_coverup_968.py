# file: lib/ansible/module_utils/urls.py:1458-1466
# asked: {"lines": [1458, 1466], "branches": []}
# gained: {"lines": [1458, 1466], "branches": []}

import pytest
from ansible.module_utils.urls import Request
from unittest.mock import patch

@pytest.fixture
def request_instance():
    return Request()

def test_options_method(request_instance):
    url = 'http://example.com'
    with patch.object(request_instance, 'open', return_value='mocked_response') as mock_open:
        response = request_instance.options(url)
        mock_open.assert_called_once_with('OPTIONS', url)
        assert response == 'mocked_response'
