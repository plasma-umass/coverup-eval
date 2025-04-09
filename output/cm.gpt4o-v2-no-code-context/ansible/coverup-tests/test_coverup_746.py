# file: lib/ansible/galaxy/api.py:180-181
# asked: {"lines": [180, 181], "branches": []}
# gained: {"lines": [180, 181], "branches": []}

import pytest
from ansible.galaxy.api import _urljoin
from ansible.module_utils._text import to_native

def test_urljoin_with_multiple_args():
    result = _urljoin('http://example.com', 'path', 'to', 'resource')
    assert result == 'http://example.com/path/to/resource'

def test_urljoin_with_empty_string():
    result = _urljoin('http://example.com', '', 'resource')
    assert result == 'http://example.com/resource'

def test_urljoin_with_trailing_slash():
    result = _urljoin('http://example.com/', 'path/')
    assert result == 'http://example.com/path'

def test_urljoin_with_none():
    result = _urljoin('http://example.com', None, 'resource')
    assert result == 'http://example.com/resource'

def test_urljoin_with_special_characters():
    result = _urljoin('http://example.com', 'path with spaces', 'resource')
    assert result == 'http://example.com/path with spaces/resource'
