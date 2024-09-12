# file: lib/ansible/plugins/filter/urlsplit.py:14-25
# asked: {"lines": [14, 16, 20, 21, 22, 23, 25], "branches": [[20, 21], [20, 25], [21, 22], [21, 23]]}
# gained: {"lines": [14, 16, 20, 21, 22, 23, 25], "branches": [[20, 21], [20, 25], [21, 22], [21, 23]]}

import pytest
from ansible.plugins.filter.urlsplit import split_url
from ansible.errors import AnsibleFilterError
from urllib.parse import urlsplit

def test_split_url_full_coverage():
    # Test with a full URL and no query
    url = 'http://example.com:80/path?query=arg#fragment'
    result = split_url(url)
    expected_result = {
        'scheme': 'http',
        'netloc': 'example.com:80',
        'path': '/path',
        'query': 'query=arg',
        'fragment': 'fragment',
        'username': None,
        'password': None,
        'hostname': 'example.com',
        'port': 80
    }
    assert result == expected_result

    # Test with a valid query
    assert split_url(url, 'scheme') == 'http'
    assert split_url(url, 'netloc') == 'example.com:80'
    assert split_url(url, 'path') == '/path'
    assert split_url(url, 'query') == 'query=arg'
    assert split_url(url, 'fragment') == 'fragment'
    assert split_url(url, 'username') is None
    assert split_url(url, 'password') is None
    assert split_url(url, 'hostname') == 'example.com'
    assert split_url(url, 'port') == 80

    # Test with an invalid query
    with pytest.raises(AnsibleFilterError, match='urlsplit: unknown URL component: invalid'):
        split_url(url, 'invalid')

    # Test with a URL without a port
    url_no_port = 'http://example.com/path?query=arg#fragment'
    result_no_port = split_url(url_no_port)
    expected_result_no_port = {
        'scheme': 'http',
        'netloc': 'example.com',
        'path': '/path',
        'query': 'query=arg',
        'fragment': 'fragment',
        'username': None,
        'password': None,
        'hostname': 'example.com',
        'port': None
    }
    assert result_no_port == expected_result_no_port

    # Test with a URL without a fragment
    url_no_fragment = 'http://example.com:80/path?query=arg'
    result_no_fragment = split_url(url_no_fragment)
    expected_result_no_fragment = {
        'scheme': 'http',
        'netloc': 'example.com:80',
        'path': '/path',
        'query': 'query=arg',
        'fragment': '',
        'username': None,
        'password': None,
        'hostname': 'example.com',
        'port': 80
    }
    assert result_no_fragment == expected_result_no_fragment

    # Test with a URL without a query
    url_no_query = 'http://example.com:80/path#fragment'
    result_no_query = split_url(url_no_query)
    expected_result_no_query = {
        'scheme': 'http',
        'netloc': 'example.com:80',
        'path': '/path',
        'query': '',
        'fragment': 'fragment',
        'username': None,
        'password': None,
        'hostname': 'example.com',
        'port': 80
    }
    assert result_no_query == expected_result_no_query
