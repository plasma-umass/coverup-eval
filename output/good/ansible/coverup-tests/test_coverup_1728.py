# file lib/ansible/utils/collection_loader/_collection_finder.py:232-238
# lines []
# branches ['236->exit']

import pytest
from ansible.utils.collection_loader import _collection_finder
from ansible.module_utils.six import PY3

# Mocking the to_native function and the FileFinder class
def test_ansible_path_hook_finder_init_py2(mocker):
    # Setup
    mocker.patch.object(_collection_finder, 'to_native', return_value='native_path')
    mocker.patch('ansible.utils.collection_loader._collection_finder.PY3', new=False)

    # Test
    path_hook_finder = _collection_finder._AnsiblePathHookFinder(collection_finder=None, pathctx='path_context')

    # Assertions
    assert path_hook_finder._pathctx == 'native_path'
    assert path_hook_finder._collection_finder is None
    assert not hasattr(path_hook_finder, '_file_finder')

    # Cleanup is not necessary as the test does not modify any global state

@pytest.mark.skipif(not PY3, reason="Test only applicable to Python 3")
def test_ansible_path_hook_finder_init_py3(mocker):
    # Setup
    mocker.patch.object(_collection_finder, 'to_native', return_value='native_path')
    mocker.patch('ansible.utils.collection_loader._collection_finder.PY3', new=True)

    # Test
    path_hook_finder = _collection_finder._AnsiblePathHookFinder(collection_finder=None, pathctx='path_context')

    # Assertions
    assert path_hook_finder._pathctx == 'native_path'
    assert path_hook_finder._collection_finder is None
    assert hasattr(path_hook_finder, '_file_finder')
    assert path_hook_finder._file_finder is None

    # Cleanup is not necessary as the test does not modify any global state
