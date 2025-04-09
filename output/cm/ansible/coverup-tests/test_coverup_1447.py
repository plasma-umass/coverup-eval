# file lib/ansible/utils/collection_loader/_collection_config.py:76-79
# lines [79]
# branches []

import pytest
from ansible.utils.collection_loader._collection_config import _AnsibleCollectionConfig

@pytest.fixture
def ansible_collection_config():
    class CollectionConfig(metaclass=_AnsibleCollectionConfig):
        pass
    return CollectionConfig

def test_default_collection_setter(ansible_collection_config):
    original_value = ansible_collection_config._default_collection
    try:
        ansible_collection_config.default_collection = 'test.collection'
        assert ansible_collection_config._default_collection == 'test.collection'
    finally:
        # Clean up by resetting to the original value
        ansible_collection_config.default_collection = original_value
