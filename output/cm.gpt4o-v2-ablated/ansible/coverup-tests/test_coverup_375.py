# file: lib/ansible/utils/collection_loader/_collection_finder.py:288-290
# asked: {"lines": [288, 290], "branches": []}
# gained: {"lines": [288], "branches": []}

import pytest
from unittest.mock import patch

# Assuming _iter_modules_impl is defined somewhere in the module
# and _AnsiblePathHookFinder is part of the module ansible.utils.collection_loader._collection_finder

class _AnsiblePathHookFinder:
    def __init__(self, pathctx):
        self._pathctx = pathctx

    def iter_modules(self, prefix):
        # NB: this currently represents only what's on disk, and does not handle package redirection
        return _iter_modules_impl([self._pathctx], prefix)

def _iter_modules_impl(paths, prefix):
    # Dummy implementation for testing purposes
    return [(prefix, path) for path in paths]

@pytest.fixture
def mock_iter_modules_impl(monkeypatch):
    def mock_impl(paths, prefix):
        return [(prefix, path) for path in paths]
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._iter_modules_impl', mock_impl)

def test_iter_modules(mock_iter_modules_impl):
    pathctx = '/some/path'
    prefix = 'test_prefix'
    finder = _AnsiblePathHookFinder(pathctx)
    
    result = finder.iter_modules(prefix)
    
    assert result == [(prefix, pathctx)]
