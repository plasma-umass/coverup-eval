# file lib/ansible/utils/collection_loader/_collection_config.py:67-70
# lines [69, 70]
# branches []

import pytest
from ansible.utils.collection_loader import _collection_config

# Assuming the _collection_config module has the following structure
# (since the actual implementation is not provided):

class _AnsibleCollectionConfig(metaclass=_collection_config._AnsibleCollectionConfig):
    _collection_finder = None

    @classmethod
    def _require_finder(cls):
        if cls._collection_finder is None:
            raise ValueError("Finder is not set")

# The test should mock the _collection_finder and its _n_collection_paths attribute
# and then access the collection_paths property to cover lines 69-70.

class CollectionFinderMock:
    _n_collection_paths = ['/path/to/collections']

def test_collection_paths_property(mocker):
    # Mock the _collection_finder and its _n_collection_paths attribute
    mocker.patch.object(_AnsibleCollectionConfig, '_collection_finder', new=CollectionFinderMock())

    # Access the collection_paths property to execute lines 69-70
    paths = _AnsibleCollectionConfig.collection_paths

    # Verify the postcondition that the paths are correctly returned
    assert paths == ['/path/to/collections']

    # Clean up is handled by pytest-mock through the mocker fixture
