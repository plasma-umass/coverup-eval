# file lib/ansible/utils/collection_loader/_collection_finder.py:110-128
# lines [128]
# branches ['127->128']

import sys
import pytest
from ansible.utils.collection_loader import _collection_finder

class MockAnsibleCollectionConfig:
    _collection_finder = None

    @classmethod
    def collection_finder(cls):
        return cls._collection_finder

def test_ansible_collection_finder_remove_failure(mocker):
    # Setup the test environment
    finder = _collection_finder._AnsibleCollectionFinder()
    sys.meta_path.append(finder)
    sys.path_hooks.append(finder)
    mocker.patch.object(_collection_finder, 'AnsibleCollectionConfig', MockAnsibleCollectionConfig)
    MockAnsibleCollectionConfig._collection_finder = finder

    # Ensure the setup is correct
    assert _collection_finder.AnsibleCollectionConfig.collection_finder() is finder

    # Perform the action that should be tested
    with pytest.raises(AssertionError):
        _collection_finder._AnsibleCollectionFinder._remove()

    # Cleanup after test to not affect other tests
    if finder in sys.meta_path:
        sys.meta_path.remove(finder)
    if finder in sys.path_hooks:
        sys.path_hooks.remove(finder)
    _collection_finder.AnsibleCollectionConfig._collection_finder = None
