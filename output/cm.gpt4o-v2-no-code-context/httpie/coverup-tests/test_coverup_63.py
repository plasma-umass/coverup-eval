# file: httpie/client.py:300-324
# asked: {"lines": [300, 317, 318, 320, 321, 323, 324], "branches": []}
# gained: {"lines": [300, 317, 318, 320, 321, 323, 324], "branches": []}

import pytest
from httpie.client import ensure_path_as_is
from urllib.parse import urlparse, urlunparse

def test_ensure_path_as_is_basic():
    orig_url = 'http://foo/../'
    prepped_url = 'http://foo/?foo=bar'
    expected = 'http://foo/../?foo=bar'
    result = ensure_path_as_is(orig_url, prepped_url)
    assert result == expected

def test_ensure_path_as_is_with_different_paths():
    orig_url = 'http://example.com/newpath'
    prepped_url = 'http://example.com/oldpath?query=1'
    expected = 'http://example.com/newpath?query=1'
    result = ensure_path_as_is(orig_url, prepped_url)
    assert result == expected

def test_ensure_path_as_is_with_no_path():
    orig_url = 'http://example.com'
    prepped_url = 'http://example.com/oldpath?query=1'
    expected = 'http://example.com?query=1'
    result = ensure_path_as_is(orig_url, prepped_url)
    assert result == expected

def test_ensure_path_as_is_with_complex_url():
    orig_url = 'http://user:pass@host:1234/newpath;params?query=1#fragment'
    prepped_url = 'http://user:pass@host:1234/oldpath;params?query=2#fragment'
    expected = 'http://user:pass@host:1234/newpath;params?query=2#fragment'
    result = ensure_path_as_is(orig_url, prepped_url)
    assert result == expected

def test_ensure_path_as_is_with_empty_path():
    orig_url = 'http://example.com'
    prepped_url = 'http://example.com?query=1'
    expected = 'http://example.com?query=1'
    result = ensure_path_as_is(orig_url, prepped_url)
    assert result == expected
