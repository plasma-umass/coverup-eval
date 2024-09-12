# file: lib/ansible/utils/collection_loader/_collection_finder.py:241-250
# asked: {"lines": [247], "branches": [[243, 250], [246, 247]]}
# gained: {"lines": [247], "branches": [[246, 247]]}

import pytest
import sys
from ansible.module_utils.six import PY3
from ansible.utils.collection_loader._collection_finder import _AnsiblePathHookFinder

def test_get_filefinder_path_hook_py3(monkeypatch):
    if not PY3:
        pytest.skip("Test only applicable for Python 3")

    # Mock sys.path_hooks to control the environment
    class MockFileFinder:
        def __repr__(self):
            return "FileFinder"

    class MockOtherFinder:
        def __repr__(self):
            return "OtherFinder"

    # Test case where there is exactly one FileFinder
    monkeypatch.setattr(sys, 'path_hooks', [MockFileFinder()])
    finder = _AnsiblePathHookFinder(None, None)
    hook = finder._get_filefinder_path_hook()
    assert hook.__repr__() == "FileFinder"

    # Test case where there are no FileFinders
    monkeypatch.setattr(sys, 'path_hooks', [MockOtherFinder()])
    finder = _AnsiblePathHookFinder(None, None)
    with pytest.raises(Exception, match="need exactly one FileFinder import hook"):
        finder._get_filefinder_path_hook()

    # Test case where there are multiple FileFinders
    monkeypatch.setattr(sys, 'path_hooks', [MockFileFinder(), MockFileFinder()])
    finder = _AnsiblePathHookFinder(None, None)
    with pytest.raises(Exception, match="need exactly one FileFinder import hook"):
        finder._get_filefinder_path_hook()
