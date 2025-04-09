# file: httpie/client.py:135-144
# asked: {"lines": [139, 140, 141, 142, 144], "branches": []}
# gained: {"lines": [139, 140, 141, 142, 144], "branches": []}

import http.client
import pytest
from contextlib import contextmanager
from httpie.client import max_headers

def test_max_headers_limit(monkeypatch):
    original_max_headers = http.client._MAXHEADERS

    with max_headers(10):
        assert http.client._MAXHEADERS == 10

    assert http.client._MAXHEADERS == original_max_headers

def test_max_headers_no_limit(monkeypatch):
    original_max_headers = http.client._MAXHEADERS

    with max_headers(None):
        assert http.client._MAXHEADERS == float('Inf')

    assert http.client._MAXHEADERS == original_max_headers
