# file httpie/client.py:300-324
# lines [300, 317, 318, 320, 321, 323, 324]
# branches []

import pytest
from urllib.parse import urlparse, urlunparse
from httpie.client import ensure_path_as_is

def test_ensure_path_as_is():
    orig_url = 'http://foo/../'
    prepped_url = 'http://foo/?foo=bar'
    expected_url = 'http://foo/../?foo=bar'
    
    result = ensure_path_as_is(orig_url, prepped_url)
    
    assert result == expected_url

    # Additional test cases to ensure full coverage
    orig_url = 'http://example.com/path/to/resource'
    prepped_url = 'http://example.com/another/path?query=1'
    expected_url = 'http://example.com/path/to/resource?query=1'
    
    result = ensure_path_as_is(orig_url, prepped_url)
    
    assert result == expected_url

    orig_url = 'https://secure.example.com/secure/path'
    prepped_url = 'https://secure.example.com/other/path?secure=true'
    expected_url = 'https://secure.example.com/secure/path?secure=true'
    
    result = ensure_path_as_is(orig_url, prepped_url)
    
    assert result == expected_url
