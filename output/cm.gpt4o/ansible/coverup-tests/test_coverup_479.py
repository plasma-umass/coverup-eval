# file lib/ansible/galaxy/api.py:131-142
# lines [131, 133, 135, 136, 137, 138, 139, 142]
# branches []

import pytest
from urllib.parse import urlparse
from ansible.galaxy.api import get_cache_id

def test_get_cache_id_valid_url():
    url = "http://example.com:8080/path"
    expected_cache_id = "example.com:8080"
    assert get_cache_id(url) == expected_cache_id

def test_get_cache_id_no_port():
    url = "http://example.com/path"
    expected_cache_id = "example.com:"
    assert get_cache_id(url) == expected_cache_id

def test_get_cache_id_invalid_port(mocker):
    url = "http://example.com:invalid_port/path"
    mocker.patch('urllib.parse.urlparse', return_value=urlparse(url))
    expected_cache_id = "example.com:"
    assert get_cache_id(url) == expected_cache_id
