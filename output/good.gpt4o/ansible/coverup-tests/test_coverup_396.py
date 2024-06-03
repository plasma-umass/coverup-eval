# file lib/ansible/plugins/filter/urlsplit.py:14-25
# lines [14, 16, 20, 21, 22, 23, 25]
# branches ['20->21', '20->25', '21->22', '21->23']

import pytest
from ansible.plugins.filter.urlsplit import split_url
from ansible.errors import AnsibleFilterError

def test_split_url_full_coverage():
    # Test with a valid URL and no query
    url = 'http://example.com/path?query=1#fragment'
    result = split_url(url)
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'example.com'
    assert result['path'] == '/path'
    assert result['query'] == 'query=1'
    assert result['fragment'] == 'fragment'

    # Test with a valid URL and a valid query
    result = split_url(url, query='scheme')
    assert result == 'http'

    # Test with a valid URL and an invalid query
    with pytest.raises(AnsibleFilterError, match='urlsplit: unknown URL component: invalid'):
        split_url(url, query='invalid')

    # Test with a URL that has no scheme
    url = '//example.com/path'
    result = split_url(url)
    assert result['scheme'] == ''
    assert result['netloc'] == 'example.com'
    assert result['path'] == '/path'

    # Test with a URL that has no path
    url = 'http://example.com'
    result = split_url(url)
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'example.com'
    assert result['path'] == ''
