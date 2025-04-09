# file: lib/ansible/utils/collection_loader/_collection_finder.py:232-238
# asked: {"lines": [232, 234, 235, 236, 238], "branches": [[236, 0], [236, 238]]}
# gained: {"lines": [232, 234, 235, 236, 238], "branches": [[236, 0], [236, 238]]}

import pytest
from unittest.mock import Mock, patch
from ansible.utils.collection_loader._collection_finder import _AnsiblePathHookFinder
from ansible.module_utils._text import to_native

@pytest.fixture
def mock_collection_finder():
    return Mock()

@pytest.fixture
def mock_pathctx():
    return Mock()

def test_ansible_path_hook_finder_init_py3(mock_collection_finder, mock_pathctx, monkeypatch):
    # Ensure PY3 is True
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder.PY3', True)
    
    # Create instance of _AnsiblePathHookFinder
    finder = _AnsiblePathHookFinder(mock_collection_finder, mock_pathctx)
    
    # Assertions to verify the state
    assert finder._pathctx == to_native(mock_pathctx)
    assert finder._collection_finder == mock_collection_finder
    assert finder._file_finder is None

def test_ansible_path_hook_finder_init_py2(mock_collection_finder, mock_pathctx, monkeypatch):
    # Ensure PY3 is False
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder.PY3', False)
    
    # Create instance of _AnsiblePathHookFinder
    finder = _AnsiblePathHookFinder(mock_collection_finder, mock_pathctx)
    
    # Assertions to verify the state
    assert finder._pathctx == to_native(mock_pathctx)
    assert finder._collection_finder == mock_collection_finder
    assert not hasattr(finder, '_file_finder')
