# file: lib/ansible/utils/collection_loader/_collection_config.py:56-58
# asked: {"lines": [56, 57, 58], "branches": []}
# gained: {"lines": [56, 57, 58], "branches": []}

import pytest

# Assuming the class _AnsibleCollectionConfig is defined in ansible/utils/collection_loader/_collection_config.py
from ansible.utils.collection_loader._collection_config import _AnsibleCollectionConfig

class TestAnsibleCollectionConfig:
    
    def test_collection_finder_property(self, monkeypatch):
        # Create a dummy class to use the metaclass
        class DummyClass(metaclass=_AnsibleCollectionConfig):
            pass

        # Use monkeypatch to set the _collection_finder attribute
        monkeypatch.setattr(DummyClass, '_collection_finder', 'dummy_finder')

        # Assert that the property returns the correct value
        assert DummyClass.collection_finder == "dummy_finder"
