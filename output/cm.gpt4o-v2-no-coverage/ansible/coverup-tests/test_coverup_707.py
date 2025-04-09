# file: lib/ansible/utils/collection_loader/_collection_finder.py:130-136
# asked: {"lines": [130, 131, 132, 134, 136], "branches": []}
# gained: {"lines": [130, 131, 132, 134, 136], "branches": []}

import pytest
import sys
from ansible.utils.collection_loader._collection_config import AnsibleCollectionConfig
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder

@pytest.fixture
def setup_finder():
    finder = _AnsibleCollectionFinder()
    yield finder
    # Cleanup after test
    finder._remove()

def test_install(setup_finder, mocker):
    finder = setup_finder

    # Mock the _ansible_collection_path_hook to avoid side effects
    mocker.patch.object(finder, '_ansible_collection_path_hook', return_value=None)

    # Ensure initial state
    assert finder not in sys.meta_path
    assert finder._ansible_collection_path_hook not in sys.path_hooks
    assert AnsibleCollectionConfig.collection_finder is None

    # Call the _install method
    finder._install()

    # Assertions to verify postconditions
    assert sys.meta_path[0] is finder
    assert sys.path_hooks[0] is finder._ansible_collection_path_hook
    assert AnsibleCollectionConfig.collection_finder is finder

def test_remove(setup_finder):
    finder = setup_finder

    # Add finder to sys.meta_path and sys.path_hooks to test removal
    sys.meta_path.insert(0, finder)
    sys.path_hooks.insert(0, finder._ansible_collection_path_hook)
    AnsibleCollectionConfig.collection_finder = finder

    # Ensure initial state
    assert finder in sys.meta_path
    assert finder._ansible_collection_path_hook in sys.path_hooks
    assert AnsibleCollectionConfig.collection_finder is finder

    # Call the _remove method
    finder._remove()

    # Assertions to verify postconditions
    assert finder not in sys.meta_path
    assert finder._ansible_collection_path_hook not in sys.path_hooks
    assert AnsibleCollectionConfig.collection_finder is None
