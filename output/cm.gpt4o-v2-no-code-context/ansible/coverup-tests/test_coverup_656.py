# file: lib/ansible/utils/collection_loader/_collection_config.py:72-74
# asked: {"lines": [72, 73, 74], "branches": []}
# gained: {"lines": [72, 73, 74], "branches": []}

import pytest

# Assuming the class _AnsibleCollectionConfig is defined in ansible/utils/collection_loader/_collection_config.py
from ansible.utils.collection_loader._collection_config import _AnsibleCollectionConfig

class TestAnsibleCollectionConfig:
    
    def test_default_collection_property(self, monkeypatch):
        # Create a mock class to simulate the _default_collection attribute
        class MockCollectionConfig(metaclass=_AnsibleCollectionConfig):
            pass
        
        # Use monkeypatch to set the _default_collection attribute
        monkeypatch.setattr(MockCollectionConfig, '_default_collection', 'mock_default_collection')
        
        # Assert that the default_collection property returns the correct value
        assert MockCollectionConfig.default_collection == 'mock_default_collection'
