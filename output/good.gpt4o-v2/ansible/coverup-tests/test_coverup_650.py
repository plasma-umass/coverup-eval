# file: lib/ansible/plugins/filter/urlsplit.py:29-35
# asked: {"lines": [29, 30, 32, 33, 34], "branches": []}
# gained: {"lines": [29, 30, 32, 33, 34], "branches": []}

import pytest
from ansible.plugins.filter.urlsplit import FilterModule, split_url
from ansible.errors import AnsibleFilterError

def test_filter_module_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    assert 'urlsplit' in filters
    assert filters['urlsplit'] == split_url

def test_split_url_with_query():
    url = 'http://example.com/path?query=1'
    result = split_url(url, query='scheme')
    assert result == 'http'

def test_split_url_without_query():
    url = 'http://example.com/path?query=1'
    result = split_url(url)
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'example.com'
    assert result['path'] == '/path'
    assert result['query'] == 'query=1'

def test_split_url_with_invalid_query():
    url = 'http://example.com/path?query=1'
    with pytest.raises(AnsibleFilterError, match='unknown URL component'):
        split_url(url, query='invalid_component')
