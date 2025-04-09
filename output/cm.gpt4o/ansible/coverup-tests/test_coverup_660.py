# file lib/ansible/utils/collection_loader/_collection_config.py:51-54
# lines [51, 52, 53, 54]
# branches []

import pytest
from unittest.mock import patch

# Assuming the class _AnsibleCollectionConfig is defined in ansible.utils.collection_loader._collection_config
from ansible.utils.collection_loader._collection_config import _AnsibleCollectionConfig, _EventSource

def test_ansible_collection_config_init():
    with patch('ansible.utils.collection_loader._collection_config._EventSource') as MockEventSource:
        MockEventSource.return_value = _EventSource()
        
        class TestClass(metaclass=_AnsibleCollectionConfig):
            pass
        
        assert TestClass._collection_finder is None
        assert TestClass._default_collection is None
        assert isinstance(TestClass._on_collection_load, _EventSource)
