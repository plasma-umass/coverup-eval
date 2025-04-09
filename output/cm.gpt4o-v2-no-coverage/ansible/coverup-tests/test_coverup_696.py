# file: lib/ansible/plugins/filter/urlsplit.py:29-35
# asked: {"lines": [29, 30, 32, 33, 34], "branches": []}
# gained: {"lines": [29, 30, 32, 33, 34], "branches": []}

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.urlsplit import FilterModule, split_url

class TestFilterModule:
    def test_filters(self):
        filter_module = FilterModule()
        filters = filter_module.filters()
        assert 'urlsplit' in filters
        assert filters['urlsplit'] == split_url

class TestSplitUrl:
    def test_split_url_no_query(self):
        url = 'http://example.com/path?query=1#fragment'
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

    def test_split_url_with_query(self):
        url = 'http://example.com/path?query=1#fragment'
        result = split_url(url, query='scheme')
        assert result == 'http'

    def test_split_url_with_invalid_query(self):
        url = 'http://example.com/path?query=1#fragment'
        with pytest.raises(AnsibleFilterError, match='urlsplit: unknown URL component: invalid'):
            split_url(url, query='invalid')
