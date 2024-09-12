# file: httpie/client.py:300-324
# asked: {"lines": [300, 317, 318, 320, 321, 323, 324], "branches": []}
# gained: {"lines": [300, 317, 318, 320, 321, 323, 324], "branches": []}

import pytest
from httpie.client import ensure_path_as_is

def test_ensure_path_as_is():
    orig_url = 'http://foo/../'
    prepped_url = 'http://foo/?foo=bar'
    expected_url = 'http://foo/../?foo=bar'
    
    result = ensure_path_as_is(orig_url, prepped_url)
    
    assert result == expected_url

def test_ensure_path_as_is_with_different_paths():
    orig_url = 'http://example.com/path1'
    prepped_url = 'http://example.com/path2?query=1'
    expected_url = 'http://example.com/path1?query=1'
    
    result = ensure_path_as_is(orig_url, prepped_url)
    
    assert result == expected_url

def test_ensure_path_as_is_with_no_path_in_prepped_url():
    orig_url = 'http://example.com/path1'
    prepped_url = 'http://example.com?query=1'
    expected_url = 'http://example.com/path1?query=1'
    
    result = ensure_path_as_is(orig_url, prepped_url)
    
    assert result == expected_url

def test_ensure_path_as_is_with_no_path_in_orig_url():
    orig_url = 'http://example.com'
    prepped_url = 'http://example.com/path2?query=1'
    expected_url = 'http://example.com?query=1'
    
    result = ensure_path_as_is(orig_url, prepped_url)
    
    assert result == expected_url

def test_ensure_path_as_is_with_empty_paths():
    orig_url = 'http://example.com'
    prepped_url = 'http://example.com'
    expected_url = 'http://example.com'
    
    result = ensure_path_as_is(orig_url, prepped_url)
    
    assert result == expected_url
