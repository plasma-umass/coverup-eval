# file lib/ansible/utils/collection_loader/_collection_finder.py:292-293
# lines [293]
# branches []

import pytest
from ansible.utils.collection_loader import _collection_finder

def test_ansible_path_hook_finder_repr():
    # Create an instance of the _AnsiblePathHookFinder
    test_path = '/test/path'
    hook_finder = _collection_finder._AnsiblePathHookFinder(collection_finder=None, pathctx=test_path)
    
    # Call the __repr__ method and assert the result is as expected
    expected_repr = "_AnsiblePathHookFinder(path='/test/path')"
    assert repr(hook_finder) == expected_repr
