# file: lib/ansible/utils/collection_loader/_collection_finder.py:232-238
# asked: {"lines": [], "branches": [[236, 0]]}
# gained: {"lines": [], "branches": [[236, 0]]}

import pytest
from unittest.mock import Mock, patch
from ansible.utils.collection_loader._collection_finder import _AnsiblePathHookFinder
from ansible.module_utils.six import PY3

@pytest.fixture
def mock_to_native():
    with patch('ansible.utils.collection_loader._collection_finder.to_native', return_value='mocked_pathctx') as mock:
        yield mock

def test_ansible_path_hook_finder_init_py3(mock_to_native):
    collection_finder = Mock()
    pathctx = 'some_path'

    with patch('ansible.utils.collection_loader._collection_finder.PY3', True):
        finder = _AnsiblePathHookFinder(collection_finder, pathctx)
        assert finder._file_finder is None
        assert finder._pathctx == 'mocked_pathctx'
        assert finder._collection_finder == collection_finder

def test_ansible_path_hook_finder_init_not_py3(mock_to_native):
    collection_finder = Mock()
    pathctx = 'some_path'

    with patch('ansible.utils.collection_loader._collection_finder.PY3', False):
        finder = _AnsiblePathHookFinder(collection_finder, pathctx)
        assert not hasattr(finder, '_file_finder')
        assert finder._pathctx == 'mocked_pathctx'
        assert finder._collection_finder == collection_finder
