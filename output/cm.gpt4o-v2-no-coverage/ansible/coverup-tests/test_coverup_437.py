# file: lib/ansible/plugins/filter/urlsplit.py:14-25
# asked: {"lines": [14, 16, 20, 21, 22, 23, 25], "branches": [[20, 21], [20, 25], [21, 22], [21, 23]]}
# gained: {"lines": [14, 16, 20, 21, 22, 23, 25], "branches": [[20, 21], [20, 25], [21, 22], [21, 23]]}

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.urlsplit import split_url

def test_split_url_no_query():
    url = "http://example.com/path?query=1#fragment"
    expected_result = {
        'scheme': 'http',
        'netloc': 'example.com',
        'path': '/path',
        'query': 'query=1',
        'fragment': 'fragment',
        'username': None,
        'password': None,
        'hostname': 'example.com',
        'port': None
    }
    result = split_url(url)
    assert result == expected_result

def test_split_url_with_valid_query():
    url = "http://example.com/path?query=1#fragment"
    result = split_url(url, query='scheme')
    assert result == 'http'

def test_split_url_with_invalid_query():
    url = "http://example.com/path?query=1#fragment"
    with pytest.raises(AnsibleFilterError) as excinfo:
        split_url(url, query='invalid')
    assert 'urlsplit: unknown URL component: invalid' in str(excinfo.value)

def test_split_url_with_alias():
    url = "http://example.com/path?query=1#fragment"
    with pytest.raises(AnsibleFilterError) as excinfo:
        split_url(url, query='invalid', alias='custom_alias')
    assert 'custom_alias: unknown URL component: invalid' in str(excinfo.value)
