# file: httpie/client.py:300-324
# asked: {"lines": [300, 317, 318, 320, 321, 323, 324], "branches": []}
# gained: {"lines": [300, 317, 318, 320, 321, 323, 324], "branches": []}

import pytest
from urllib.parse import urlparse, urlunparse
from httpie.client import ensure_path_as_is

def test_ensure_path_as_is():
    # Test case 1: Basic functionality
    orig_url = 'http://foo/../'
    prepped_url = 'http://foo/?foo=bar'
    expected = 'http://foo/../?foo=bar'
    assert ensure_path_as_is(orig_url, prepped_url) == expected

    # Test case 2: Different paths
    orig_url = 'http://example.com/path1'
    prepped_url = 'http://example.com/path2?query=1'
    expected = 'http://example.com/path1?query=1'
    assert ensure_path_as_is(orig_url, prepped_url) == expected

    # Test case 3: No path in original URL
    orig_url = 'http://example.com'
    prepped_url = 'http://example.com/path2?query=1'
    expected = 'http://example.com?query=1'
    assert ensure_path_as_is(orig_url, prepped_url) == expected

    # Test case 4: No path in prepped URL
    orig_url = 'http://example.com/path1'
    prepped_url = 'http://example.com'
    expected = 'http://example.com/path1'
    assert ensure_path_as_is(orig_url, prepped_url) == expected

    # Test case 5: Both URLs have no path
    orig_url = 'http://example.com'
    prepped_url = 'http://example.com'
    expected = 'http://example.com'
    assert ensure_path_as_is(orig_url, prepped_url) == expected

    # Test case 6: Complex URL with fragments and params
    orig_url = 'http://example.com/path1;params?query=1#fragment'
    prepped_url = 'http://example.com/path2;params2?query2=2#fragment2'
    expected = 'http://example.com/path1;params2?query2=2#fragment2'
    assert ensure_path_as_is(orig_url, prepped_url) == expected
