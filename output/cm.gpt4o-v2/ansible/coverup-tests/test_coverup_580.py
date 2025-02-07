# file: lib/ansible/utils/collection_loader/_collection_finder.py:232-238
# asked: {"lines": [232, 234, 235, 236, 238], "branches": [[236, 0], [236, 238]]}
# gained: {"lines": [232, 234, 235, 236, 238], "branches": [[236, 238]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsiblePathHookFinder
from ansible.module_utils.common.text.converters import to_native
from ansible.module_utils.six import PY3

class MockCollectionFinder:
    pass

@pytest.fixture
def mock_collection_finder():
    return MockCollectionFinder()

def test_ansible_path_hook_finder_init_py3(mock_collection_finder, mocker):
    mocker.patch('ansible.module_utils.six.PY3', True)
    pathctx = 'some_path'
    finder = _AnsiblePathHookFinder(mock_collection_finder, pathctx)
    
    assert finder._pathctx == to_native(pathctx)
    assert finder._collection_finder == mock_collection_finder
    assert finder._file_finder is None

def test_ansible_path_hook_finder_init_not_py3(mock_collection_finder, mocker):
    mocker.patch('ansible.module_utils.six.PY3', False)
    pathctx = 'some_path'
    finder = _AnsiblePathHookFinder(mock_collection_finder, pathctx)
    
    assert finder._pathctx == to_native(pathctx)
    assert finder._collection_finder == mock_collection_finder
    assert finder._file_finder is None
