# file: httpie/client.py:300-324
# asked: {"lines": [317, 318, 320, 321, 323, 324], "branches": []}
# gained: {"lines": [317, 318, 320, 321, 323, 324], "branches": []}

import pytest
from urllib.parse import urlparse, urlunparse
from httpie.client import ensure_path_as_is

def test_ensure_path_as_is_basic():
    orig_url = 'http://foo/../'
    prepped_url = 'http://foo/?foo=bar'
    expected = 'http://foo/../?foo=bar'
    result = ensure_path_as_is(orig_url, prepped_url)
    assert result == expected

def test_ensure_path_as_is_with_port():
    orig_url = 'http://foo:8080/../'
    prepped_url = 'http://foo:8080/?foo=bar'
    expected = 'http://foo:8080/../?foo=bar'
    result = ensure_path_as_is(orig_url, prepped_url)
    assert result == expected

def test_ensure_path_as_is_with_fragment():
    orig_url = 'http://foo/../#fragment'
    prepped_url = 'http://foo/?foo=bar#fragment'
    expected = 'http://foo/../?foo=bar#fragment'
    result = ensure_path_as_is(orig_url, prepped_url)
    assert result == expected

def test_ensure_path_as_is_with_userinfo():
    orig_url = 'http://user:pass@foo/../'
    prepped_url = 'http://user:pass@foo/?foo=bar'
    expected = 'http://user:pass@foo/../?foo=bar'
    result = ensure_path_as_is(orig_url, prepped_url)
    assert result == expected

def test_ensure_path_as_is_with_query():
    orig_url = 'http://foo/../?original=query'
    prepped_url = 'http://foo/?foo=bar'
    expected = 'http://foo/../?foo=bar'
    result = ensure_path_as_is(orig_url, prepped_url)
    assert result == expected

def test_ensure_path_as_is_with_different_paths():
    orig_url = 'http://foo/bar'
    prepped_url = 'http://foo/baz?foo=bar'
    expected = 'http://foo/bar?foo=bar'
    result = ensure_path_as_is(orig_url, prepped_url)
    assert result == expected
