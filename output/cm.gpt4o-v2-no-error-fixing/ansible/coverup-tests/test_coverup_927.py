# file: lib/ansible/galaxy/api.py:180-181
# asked: {"lines": [181], "branches": []}
# gained: {"lines": [181], "branches": []}

import pytest
from ansible.galaxy.api import _urljoin
from ansible.module_utils._text import to_native

def test_urljoin(monkeypatch):
    # Mock the to_native function to return the input value
    def mock_to_native(value, errors):
        return value

    monkeypatch.setattr('ansible.module_utils._text.to_native', mock_to_native)

    # Test cases to cover different scenarios
    assert _urljoin('http://example.com', 'path', 'to', 'resource') == 'http://example.com/path/to/resource'
    assert _urljoin('http://example.com/', '/path/', '/to/', '/resource/') == 'http://example.com/path/to/resource'
    assert _urljoin('http://example.com', '', 'path') == 'http://example.com/path'
    assert _urljoin('', 'path', 'to', 'resource') == 'path/to/resource'
    assert _urljoin('http://example.com', None, 'path') == 'http://example.com/path'
    assert _urljoin('http://example.com', 'path', '', 'to', 'resource') == 'http://example.com/path/to/resource'
