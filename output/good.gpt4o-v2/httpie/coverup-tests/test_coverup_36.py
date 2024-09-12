# file: httpie/client.py:135-144
# asked: {"lines": [135, 136, 139, 140, 141, 142, 144], "branches": []}
# gained: {"lines": [135, 136, 139, 140, 141, 142, 144], "branches": []}

import pytest
import http.client
from httpie.client import max_headers

def test_max_headers_with_limit():
    original_max_headers = http.client._MAXHEADERS
    limit = 10

    with max_headers(limit):
        assert http.client._MAXHEADERS == limit

    assert http.client._MAXHEADERS == original_max_headers

def test_max_headers_without_limit():
    original_max_headers = http.client._MAXHEADERS

    with max_headers(None):
        assert http.client._MAXHEADERS == float('Inf')

    assert http.client._MAXHEADERS == original_max_headers
