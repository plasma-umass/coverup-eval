# file: lib/ansible/galaxy/api.py:131-142
# asked: {"lines": [131, 133, 135, 136, 137, 138, 139, 142], "branches": []}
# gained: {"lines": [131, 133, 135, 136, 137, 142], "branches": []}

import pytest
from urllib.parse import urlparse

# Assuming the function get_cache_id is part of a class or module, we need to import it.
# For this example, let's assume it's a standalone function in a module named `api`.
from ansible.galaxy.api import get_cache_id

def test_get_cache_id_valid_url():
    url = "http://example.com:8080/path"
    expected_cache_id = "example.com:8080"
    assert get_cache_id(url) == expected_cache_id

def test_get_cache_id_no_port():
    url = "http://example.com/path"
    expected_cache_id = "example.com:"
    assert get_cache_id(url) == expected_cache_id

def test_get_cache_id_invalid_port(monkeypatch):
    url = "http://example.com:invalid_port/path"
    
    # Monkeypatch urlparse to simulate ValueError for port
    def mock_urlparse(url):
        class MockUrlInfo:
            hostname = "example.com"
            port = None
        return MockUrlInfo()
    
    monkeypatch.setattr('ansible.galaxy.api.urlparse', mock_urlparse)
    
    expected_cache_id = "example.com:"
    assert get_cache_id(url) == expected_cache_id

def test_get_cache_id_with_credentials():
    url = "http://user:pass@example.com:8080/path"
    expected_cache_id = "example.com:8080"
    assert get_cache_id(url) == expected_cache_id
