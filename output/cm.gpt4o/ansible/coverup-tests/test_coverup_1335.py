# file lib/ansible/utils/collection_loader/_collection_config.py:76-79
# lines [79]
# branches []

import pytest
from unittest.mock import patch

# Assuming the class _AnsibleCollectionConfig is defined in ansible.utils.collection_loader._collection_config
from ansible.utils.collection_loader._collection_config import _AnsibleCollectionConfig

def test_default_collection_setter():
    class TestClass(metaclass=_AnsibleCollectionConfig):
        _default_collection = None

    with patch.object(TestClass, '_default_collection', new_callable=property) as mock_default_collection:
        TestClass.default_collection = 'test_value'
        assert TestClass._default_collection == 'test_value'
