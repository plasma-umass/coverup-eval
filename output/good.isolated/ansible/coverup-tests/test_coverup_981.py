# file lib/ansible/utils/collection_loader/_collection_config.py:106-107
# lines [106, 107]
# branches []

import pytest
from ansible.utils.collection_loader import _collection_config
from ansible.utils.collection_loader._collection_config import AnsibleCollectionConfig

# Assuming the _AnsibleCollectionConfig is a metaclass defined in the same module
# and we need to test the instantiation of AnsibleCollectionConfig which uses it.

def test_ansible_collection_config_instantiation(mocker):
    # Mock the metaclass __call__ method to ensure it's being used
    mocker.patch.object(_collection_config._AnsibleCollectionConfig, '__call__', return_value=None)

    # Instantiate AnsibleCollectionConfig to trigger the metaclass __call__
    config_instance = AnsibleCollectionConfig()

    # Assert that the metaclass __call__ was indeed called
    _collection_config._AnsibleCollectionConfig.__call__.assert_called_once()

    # Clean up by unpatching the metaclass
    mocker.stopall()
