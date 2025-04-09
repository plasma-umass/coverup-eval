# file: lib/ansible/module_utils/urls.py:1448-1456
# asked: {"lines": [1448, 1456], "branches": []}
# gained: {"lines": [1448, 1456], "branches": []}

import pytest
from unittest.mock import patch, MagicMock

# Assuming the Request class is imported from ansible/module_utils/urls.py
from ansible.module_utils.urls import Request

@pytest.fixture
def request_instance():
    return Request()

def test_get_method(request_instance, monkeypatch):
    mock_response = MagicMock(name='HTTPResponse')
    
    def mock_open(method, url, **kwargs):
        assert method == 'GET'
        assert url == 'http://example.com'
        assert kwargs == {'param': 'value'}
        return mock_response
    
    monkeypatch.setattr(request_instance, 'open', mock_open)
    
    response = request_instance.get('http://example.com', param='value')
    
    assert response == mock_response
