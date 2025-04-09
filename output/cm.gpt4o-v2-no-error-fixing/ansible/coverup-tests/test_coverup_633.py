# file: lib/ansible/utils/collection_loader/_collection_finder.py:292-293
# asked: {"lines": [292, 293], "branches": []}
# gained: {"lines": [292, 293], "branches": []}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsiblePathHookFinder

def test_ansible_path_hook_finder_repr():
    # Arrange
    collection_finder = None  # or a mock if necessary
    pathctx = 'test_path'
    finder = _AnsiblePathHookFinder(collection_finder, pathctx)
    
    # Act
    repr_str = repr(finder)
    
    # Assert
    assert repr_str == "_AnsiblePathHookFinder(path='test_path')"

