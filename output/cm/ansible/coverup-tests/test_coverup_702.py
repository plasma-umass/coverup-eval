# file lib/ansible/utils/collection_loader/_collection_config.py:95-98
# lines [95, 96, 97, 98]
# branches []

import pytest
from ansible.utils.collection_loader import _collection_config

# Assuming the _collection_config module has the following structure
# (since the actual implementation is not provided in the question):

class _AnsibleCollectionConfig(metaclass=_collection_config._AnsibleCollectionConfig):
    _collection_finder = None

    @classmethod
    def _require_finder(cls):
        if cls._collection_finder is None:
            raise ValueError("Finder is required")

# Test function to cover the missing lines/branches
def test_playbook_paths_setter(mocker):
    # Mock the _require_finder method to do nothing
    mocker.patch.object(_AnsibleCollectionConfig, '_require_finder')
    # Mock the _collection_finder to verify the set_playbook_paths call
    mock_collection_finder = mocker.Mock()
    _AnsibleCollectionConfig._collection_finder = mock_collection_finder

    # Set the playbook_paths to test the setter
    test_playbook_paths = ['/path/to/playbook1', '/path/to/playbook2']
    _AnsibleCollectionConfig.playbook_paths = test_playbook_paths

    # Verify that _require_finder was called
    _AnsibleCollectionConfig._require_finder.assert_called_once()
    # Verify that set_playbook_paths was called with the correct value
    mock_collection_finder.set_playbook_paths.assert_called_once_with(test_playbook_paths)

    # Clean up by removing the mock from the class
    del _AnsibleCollectionConfig._collection_finder
