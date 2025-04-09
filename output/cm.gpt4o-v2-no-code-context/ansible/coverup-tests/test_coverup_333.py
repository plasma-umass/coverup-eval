# file: lib/ansible/plugins/filter/urlsplit.py:14-25
# asked: {"lines": [14, 16, 20, 21, 22, 23, 25], "branches": [[20, 21], [20, 25], [21, 22], [21, 23]]}
# gained: {"lines": [14, 16, 20, 21, 22, 23, 25], "branches": [[20, 21], [20, 25], [21, 22], [21, 23]]}

import pytest
from ansible.plugins.filter.urlsplit import split_url
from ansible.errors import AnsibleFilterError

def test_split_url_no_query():
    url = "http://example.com/path?query=1#fragment"
    result = split_url(url)
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'example.com'
    assert result['path'] == '/path'
    assert result['query'] == 'query=1'
    assert result['fragment'] == 'fragment'

def test_split_url_with_valid_query():
    url = "http://example.com/path?query=1#fragment"
    result = split_url(url, query='scheme')
    assert result == 'http'

def test_split_url_with_invalid_query():
    url = "http://example.com/path?query=1#fragment"
    with pytest.raises(AnsibleFilterError) as excinfo:
        split_url(url, query='invalid')
    assert 'unknown URL component' in str(excinfo.value)
