# file lib/ansible/galaxy/api.py:180-181
# lines [180, 181]
# branches []

import pytest
from ansible.galaxy.api import _urljoin

def test_urljoin(mocker):
    # Test with multiple arguments
    result = _urljoin('http://example.com', 'path', 'to', 'resource')
    assert result == 'http://example.com/path/to/resource'

    # Test with leading and trailing slashes
    result = _urljoin('/leading/slash/', '/trailing/slash/')
    assert result == 'leading/slash/trailing/slash'

    # Test with empty arguments
    result = _urljoin('', 'path', '', 'to', 'resource')
    assert result == 'path/to/resource'

    # Test with only empty arguments
    result = _urljoin('', '', '')
    assert result == ''

    # Test with special characters
    result = _urljoin('http://example.com', 'path with spaces', 'to', 'resource')
    assert result == 'http://example.com/path with spaces/to/resource'
