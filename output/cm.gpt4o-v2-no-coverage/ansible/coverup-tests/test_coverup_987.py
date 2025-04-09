# file: lib/ansible/module_utils/urls.py:1511-1519
# asked: {"lines": [1511, 1519], "branches": []}
# gained: {"lines": [1511, 1519], "branches": []}

import pytest
from ansible.module_utils.urls import Request
from unittest.mock import patch

@pytest.fixture
def request_instance():
    return Request()

def test_delete_method(request_instance):
    url = "http://example.com"
    
    with patch.object(request_instance, 'open', return_value="HTTPResponse") as mock_open:
        response = request_instance.delete(url)
        
        mock_open.assert_called_once_with('DELETE', url)
        assert response == "HTTPResponse"
