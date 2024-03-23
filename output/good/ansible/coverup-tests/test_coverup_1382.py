# file lib/ansible/utils/collection_loader/_collection_finder.py:241-250
# lines [247]
# branches ['243->250', '246->247']

import pytest
import sys
from unittest.mock import MagicMock
from ansible.utils.collection_loader._collection_finder import _AnsiblePathHookFinder

@pytest.fixture
def clean_sys_path_hooks():
    original_path_hooks = sys.path_hooks[:]
    yield
    sys.path_hooks = original_path_hooks

def test_get_filefinder_path_hook_exception(clean_sys_path_hooks, mocker):
    # Mock the sys.path_hooks to contain more than one 'FileFinder' to trigger the exception
    mock_path_hook = MagicMock()
    mocker.patch.object(mock_path_hook, '__repr__', return_value="FileFinder")
    sys.path_hooks.append(mock_path_hook)
    sys.path_hooks.append(mock_path_hook)

    # Create a mock for the _AnsiblePathHookFinder constructor arguments
    collection_finder = mocker.MagicMock()
    pathctx = mocker.MagicMock()

    finder = _AnsiblePathHookFinder(collection_finder, pathctx)

    with pytest.raises(Exception) as excinfo:
        finder._get_filefinder_path_hook()

    assert "need exactly one FileFinder import hook" in str(excinfo.value)
