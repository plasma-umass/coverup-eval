# file: lib/ansible/module_utils/urls.py:1448-1456
# asked: {"lines": [1448, 1456], "branches": []}
# gained: {"lines": [1448, 1456], "branches": []}

import pytest
from unittest.mock import patch
from ansible.module_utils.urls import Request

@pytest.fixture
def request_instance():
    return Request()

def test_get_method(request_instance):
    url = "http://example.com"
    with patch.object(request_instance, 'open', return_value="Mocked Response") as mock_open:
        response = request_instance.get(url)
        mock_open.assert_called_once_with('GET', url)
        assert response == "Mocked Response"
