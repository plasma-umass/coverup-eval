# file lib/ansible/utils/collection_loader/_collection_finder.py:241-250
# lines [247]
# branches ['243->250', '246->247']

import sys
import pytest
from unittest import mock

from ansible.utils.collection_loader._collection_finder import _AnsiblePathHookFinder

@pytest.fixture
def mock_sys_path_hooks():
    original_path_hooks = sys.path_hooks[:]
    yield sys.path_hooks
    sys.path_hooks[:] = original_path_hooks

def test_get_filefinder_path_hook_exception(mock_sys_path_hooks):
    # Mock sys.path_hooks to simulate the condition where no FileFinder is found
    mock_sys_path_hooks.clear()
    mock_sys_path_hooks.append(lambda x: x)  # Add a dummy hook that does not match 'FileFinder'

    with mock.patch('ansible.utils.collection_loader._collection_finder.PY3', True):
        finder = _AnsiblePathHookFinder.__new__(_AnsiblePathHookFinder)
        with pytest.raises(Exception) as excinfo:
            finder._get_filefinder_path_hook()
        assert 'need exactly one FileFinder import hook' in str(excinfo.value)

def test_get_filefinder_path_hook_success(mock_sys_path_hooks):
    # Mock sys.path_hooks to simulate the condition where exactly one FileFinder is found
    mock_sys_path_hooks.clear()
    mock_sys_path_hooks.append(mock.Mock(__repr__=lambda self: 'FileFinder'))

    with mock.patch('ansible.utils.collection_loader._collection_finder.PY3', True):
        finder = _AnsiblePathHookFinder.__new__(_AnsiblePathHookFinder)
        hook = finder._get_filefinder_path_hook()
        assert hook is not None
        assert 'FileFinder' in repr(hook)
