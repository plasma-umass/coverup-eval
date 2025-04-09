# file lib/ansible/plugins/filter/urlsplit.py:14-25
# lines [14, 16, 20, 21, 22, 23, 25]
# branches ['20->21', '20->25', '21->22', '21->23']

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.urlsplit import split_url

def test_split_url_with_invalid_query():
    with pytest.raises(AnsibleFilterError) as excinfo:
        split_url('http://example.com', query='invalid_component', alias='test_urlsplit')
    assert 'test_urlsplit: unknown URL component: invalid_component' in str(excinfo.value)

def test_split_url_with_valid_query():
    result = split_url('http://example.com', query='hostname', alias='test_urlsplit')
    assert result == 'example.com'

def test_split_url_without_query():
    result = split_url('http://example.com', query='', alias='test_urlsplit')
    assert isinstance(result, dict)
    assert 'hostname' in result
    assert result['hostname'] == 'example.com'
