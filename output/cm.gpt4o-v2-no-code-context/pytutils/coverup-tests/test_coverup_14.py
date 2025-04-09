# file: pytutils/urls.py:9-31
# asked: {"lines": [9, 23, 25, 26, 28, 30, 31], "branches": []}
# gained: {"lines": [9, 23, 25, 26, 28, 30, 31], "branches": []}

import pytest
from urllib import parse as urlparse
from urllib.parse import urlencode

# Assuming the function is defined in pytutils/urls.py
from pytutils.urls import update_query_params

def test_update_query_params(monkeypatch):
    # Test case 1: Update existing query parameter
    url = 'http://example.com?foo=bar&biz=baz'
    params = {'foo': 'stuff'}
    expected_url = 'http://example.com?foo=stuff&biz=baz'
    assert update_query_params(url, params) == expected_url

    # Test case 2: Add new query parameter
    url = 'http://example.com?foo=bar'
    params = {'biz': 'baz'}
    expected_url = 'http://example.com?foo=bar&biz=baz'
    assert update_query_params(url, params) == expected_url

    # Test case 3: No existing query parameters
    url = 'http://example.com'
    params = {'foo': 'bar'}
    expected_url = 'http://example.com?foo=bar'
    assert update_query_params(url, params) == expected_url

    # Test case 4: Empty params
    url = 'http://example.com?foo=bar'
    params = {}
    expected_url = 'http://example.com?foo=bar'
    assert update_query_params(url, params) == expected_url

    # Test case 5: Multiple values for a single key
    url = 'http://example.com?foo=bar'
    params = {'foo': ['bar', 'baz']}
    expected_url = 'http://example.com?foo=bar&foo=baz'
    assert update_query_params(url, params) == expected_url

    # Test case 6: Fragment in URL
    url = 'http://example.com?foo=bar#fragment'
    params = {'biz': 'baz'}
    expected_url = 'http://example.com?foo=bar&biz=baz#fragment'
    assert update_query_params(url, params) == expected_url

    # Test case 7: URL with path
    url = 'http://example.com/path?foo=bar'
    params = {'biz': 'baz'}
    expected_url = 'http://example.com/path?foo=bar&biz=baz'
    assert update_query_params(url, params) == expected_url

    # Test case 8: URL with scheme, netloc, path, query, and fragment
    url = 'http://example.com/path?foo=bar#fragment'
    params = {'biz': 'baz'}
    expected_url = 'http://example.com/path?foo=bar&biz=baz#fragment'
    assert update_query_params(url, params) == expected_url
