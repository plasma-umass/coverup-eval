# file: lib/ansible/utils/collection_loader/_collection_config.py:76-79
# asked: {"lines": [76, 77, 79], "branches": []}
# gained: {"lines": [76, 77, 79], "branches": []}

import pytest

# Assuming the class _AnsibleCollectionConfig is defined in ansible/utils/collection_loader/_collection_config.py
from ansible.utils.collection_loader._collection_config import _AnsibleCollectionConfig

class AnsibleCollectionConfig(metaclass=_AnsibleCollectionConfig):
    _default_collection = None

@pytest.fixture
def reset_default_collection():
    # Save the original value of _default_collection if it exists
    original_value = getattr(AnsibleCollectionConfig, '_default_collection', None)
    yield
    # Restore the original value of _default_collection
    if original_value is not None:
        AnsibleCollectionConfig._default_collection = original_value
    else:
        if hasattr(AnsibleCollectionConfig, '_default_collection'):
            delattr(AnsibleCollectionConfig, '_default_collection')

def test_default_collection_setter(reset_default_collection):
    # Test setting the default_collection
    new_value = 'test_collection'
    AnsibleCollectionConfig.default_collection = new_value
    assert AnsibleCollectionConfig._default_collection == new_value

def test_default_collection_setter_with_none(reset_default_collection):
    # Test setting the default_collection to None
    new_value = None
    AnsibleCollectionConfig.default_collection = new_value
    assert AnsibleCollectionConfig._default_collection == new_value
