# file: lib/ansible/utils/collection_loader/_collection_finder.py:241-250
# asked: {"lines": [247], "branches": [[243, 250], [246, 247]]}
# gained: {"lines": [247], "branches": [[246, 247]]}

import pytest
import sys
from unittest.mock import patch, Mock

from ansible.module_utils.six import PY3
from ansible.utils.collection_loader._collection_finder import _AnsiblePathHookFinder

@pytest.fixture(autouse=True)
def cleanup_sys_path_hooks():
    original_path_hooks = sys.path_hooks.copy()
    yield
    sys.path_hooks = original_path_hooks

def test_get_filefinder_path_hook_py3(monkeypatch):
    if not PY3:
        pytest.skip("Test only applicable for Python 3")

    class MockFileFinder:
        def __repr__(self):
            return 'FileFinder'

    mock_hook = MockFileFinder()
    monkeypatch.setattr(sys, 'path_hooks', [mock_hook])

    finder = _AnsiblePathHookFinder(collection_finder=Mock(), pathctx=Mock())
    result = finder._get_filefinder_path_hook()

    assert result == mock_hook

def test_get_filefinder_path_hook_py3_multiple_hooks(monkeypatch):
    if not PY3:
        pytest.skip("Test only applicable for Python 3")

    class MockFileFinder:
        def __repr__(self):
            return 'FileFinder'

    mock_hook1 = MockFileFinder()
    mock_hook2 = MockFileFinder()
    monkeypatch.setattr(sys, 'path_hooks', [mock_hook1, mock_hook2])

    finder = _AnsiblePathHookFinder(collection_finder=Mock(), pathctx=Mock())

    with pytest.raises(Exception) as excinfo:
        finder._get_filefinder_path_hook()

    assert 'need exactly one FileFinder import hook' in str(excinfo.value)

def test_get_filefinder_path_hook_py2(monkeypatch):
    if PY3:
        pytest.skip("Test only applicable for Python 2")

    finder = _AnsiblePathHookFinder(collection_finder=Mock(), pathctx=Mock())
    result = finder._get_filefinder_path_hook()

    assert result is None
