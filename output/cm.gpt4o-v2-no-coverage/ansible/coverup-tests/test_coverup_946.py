# file: lib/ansible/utils/collection_loader/_collection_finder.py:292-293
# asked: {"lines": [292, 293], "branches": []}
# gained: {"lines": [292, 293], "branches": []}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsiblePathHookFinder
from unittest.mock import Mock

def test_ansible_path_hook_finder_repr():
    collection_finder = Mock()
    pathctx = "/some/path"
    finder = _AnsiblePathHookFinder(collection_finder, pathctx)
    expected_repr = "_AnsiblePathHookFinder(path='/some/path')"
    assert repr(finder) == expected_repr

