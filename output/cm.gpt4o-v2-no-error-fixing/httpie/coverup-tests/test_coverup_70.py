# file: httpie/client.py:300-324
# asked: {"lines": [317, 318, 320, 321, 323, 324], "branches": []}
# gained: {"lines": [317, 318, 320, 321, 323, 324], "branches": []}

import pytest
from urllib.parse import urlparse
from httpie.client import ensure_path_as_is

def test_ensure_path_as_is():
    orig_url = 'http://foo/../'
    prepped_url = 'http://foo/?foo=bar'
    expected_url = 'http://foo/../?foo=bar'
    
    result = ensure_path_as_is(orig_url, prepped_url)
    
    assert result == expected_url

def test_ensure_path_as_is_with_different_paths():
    orig_url = 'http://example.com/newpath'
    prepped_url = 'http://example.com/oldpath?query=1'
    expected_url = 'http://example.com/newpath?query=1'
    
    result = ensure_path_as_is(orig_url, prepped_url)
    
    assert result == expected_url

def test_ensure_path_as_is_with_empty_path():
    orig_url = 'http://example.com/'
    prepped_url = 'http://example.com/oldpath?query=1'
    expected_url = 'http://example.com/?query=1'
    
    result = ensure_path_as_is(orig_url, prepped_url)
    
    assert result == expected_url

def test_ensure_path_as_is_with_no_path():
    orig_url = 'http://example.com'
    prepped_url = 'http://example.com/oldpath?query=1'
    expected_url = 'http://example.com?query=1'
    
    result = ensure_path_as_is(orig_url, prepped_url)
    
    assert result == expected_url
