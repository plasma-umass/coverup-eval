# file: lib/ansible/galaxy/api.py:131-142
# asked: {"lines": [131, 133, 135, 136, 137, 138, 139, 142], "branches": []}
# gained: {"lines": [131, 133, 135, 136, 137, 138, 139, 142], "branches": []}

import pytest
from ansible.module_utils.six.moves.urllib.parse import urlparse
from ansible.galaxy.api import get_cache_id

def test_get_cache_id_with_port():
    url = "http://example.com:8080"
    expected_cache_id = "example.com:8080"
    assert get_cache_id(url) == expected_cache_id

def test_get_cache_id_without_port():
    url = "http://example.com"
    expected_cache_id = "example.com:"
    assert get_cache_id(url) == expected_cache_id

def test_get_cache_id_with_invalid_port(monkeypatch):
    def mock_urlparse(url):
        class MockUrlInfo:
            hostname = "example.com"
            port = None
        return MockUrlInfo()
    
    monkeypatch.setattr("ansible.module_utils.six.moves.urllib.parse.urlparse", mock_urlparse)
    url = "http://example.com:invalid"
    expected_cache_id = "example.com:"
    assert get_cache_id(url) == expected_cache_id
