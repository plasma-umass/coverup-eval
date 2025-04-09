# file: lib/ansible/galaxy/api.py:131-142
# asked: {"lines": [131, 133, 135, 136, 137, 138, 139, 142], "branches": []}
# gained: {"lines": [131, 133, 135, 136, 137, 138, 139, 142], "branches": []}

import pytest
from ansible.module_utils.six.moves.urllib.parse import urlparse
from ansible.galaxy.api import get_cache_id

def test_get_cache_id_valid_url():
    url = "http://example.com:80"
    expected_cache_id = "example.com:80"
    assert get_cache_id(url) == expected_cache_id

def test_get_cache_id_no_port():
    url = "http://example.com"
    expected_cache_id = "example.com:"
    assert get_cache_id(url) == expected_cache_id

def test_get_cache_id_invalid_port(monkeypatch):
    class MockUrlInfo:
        hostname = "example.com"
        port = None

        def __init__(self, *args, **kwargs):
            raise ValueError("Invalid port")

    monkeypatch.setattr("ansible.module_utils.six.moves.urllib.parse.urlparse", lambda url: MockUrlInfo())
    url = "http://example.com:invalid"
    expected_cache_id = "example.com:"
    assert get_cache_id(url) == expected_cache_id
