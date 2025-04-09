# file lib/ansible/galaxy/api.py:131-142
# lines [131, 133, 135, 136, 137, 138, 139, 142]
# branches []

import pytest
from unittest.mock import patch
from urllib.parse import urlparse

# Assuming the original function is located in a module named `api` within the `galaxy` package
# and the function `get_cache_id` is a standalone function, not a method of the `GalaxyAPI` class.
from ansible.galaxy.api import get_cache_id

def test_get_cache_id_with_port():
    url_with_port = "http://example.com:8080"
    cache_id = get_cache_id(url_with_port)
    assert cache_id == "example.com:8080"

def test_get_cache_id_without_port():
    url_without_port = "http://example.com"
    cache_id = get_cache_id(url_without_port)
    assert cache_id == "example.com:"

def test_get_cache_id_with_invalid_port():
    url_with_invalid_port = "http://example.com:invalid"
    cache_id = get_cache_id(url_with_invalid_port)
    assert cache_id == "example.com:"
